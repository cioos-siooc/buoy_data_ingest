#!/usr/bin/env python3

"""

Parse XML from swob-ml and flatten

The resulting JSON looks like

{
  "result_time": "2020-01-16T20:32:15.913Z"
  "sampling_time": "2020-01-16T20:30:00.000Z",
  "rpt_typ": "110",
  "date_tm": "2020-01-16T20:30:00.000Z",
  "stn_typ": "18",
  "long": "-66.368600",
  "lat": "44.660560",
  "stn_elev": "0.000",
  "stn_nam": "West Bay of Fundy",
  "msc_id": "9300300",
  "wmo_synop_id": "44490",
  "wnd_snsr_vert_disp_2": "4",
  "max_avg_wnd_spd_pst10mts_1": "42.1",
  "avg_wnd_dir_pst10mts_2": "67",
  "avg_wnd_dir_pst10mts_1": "69",
  ...
}


"""

# TODO convert strings to numerics if needed using xmltodict postprocessor option

import json

import click
import xmltodict


def get_key_val_pairs_from_xml_elements(elements):
    """
    Iterate through json version of <elements> tags convert JSON structure to key,value pairs

    <elements>
        <element group="wind" name="wind_speed" orig-name="011012" uom="m/s" value="0.0">
            <qualifier group="element" name="statistical_significance" uom="unitless" value="average" />
            <qualifier group="element" name="time_displacement" uom="min" value="-2" />
            <qualifier group="element" name="time_duration" uom="min" value="2" />
            <qualifier group="element" name="vertical_displacement" uom="m" value="10" />
        </element>
    </elements>

    """

    results = {}
    for element in elements:
        results[element["@name"]] = element["@value"]

        if "qualifier" in element:
            # needed b/c xmltodict could make 'qualifiers' an array
            # if > 1 elements otherwise a dictionary
            if not isinstance(element["qualifier"], list):
                qualifiers = [element["qualifier"]]

            # there can be multiple qualifiers
            for qualifier in qualifiers:
                results[f"{element['@name']}_{qualifier['@name']}"] = qualifier[
                    "@value"
                ]
    return results


def replace_values(input_dict, from_value, to_value):
    "Replaces values in dictionary. Mutates source dictionary. Non-recursive"
    for key, val in input_dict.items():
        if val == from_value:
            input_dict[key] = to_value
    return input_dict


def format_as_flat_record(data):
    """
    Flattens the json structure that is created by xmltodict to make
    it more suitable for displaying as tabular data
    """
    # 'results' and 'metadata' stored at different paths in the XML.
    # results & metadata are dictionaries
    results = get_key_val_pairs_from_xml_elements(
        data["om:ObservationCollection"]["om:member"]["om:Observation"]["om:result"][
            "elements"
        ]["element"]
    )

    metadata = get_key_val_pairs_from_xml_elements(
        data["om:ObservationCollection"]["om:member"]["om:Observation"]["om:metadata"][
            "set"
        ]["identification-elements"]["element"]
    )

    # samplingTime also recorded as date_tm?
    sampling_time = data["om:ObservationCollection"]["om:member"]["om:Observation"][
        "om:samplingTime"
    ]["gml:TimeInstant"]["gml:timePosition"]

    result_time = data["om:ObservationCollection"]["om:member"]["om:Observation"][
        "om:resultTime"
    ]["gml:TimeInstant"]["gml:timePosition"]

    # combine all of these
    record = {
        **metadata,
        "sampling_time": sampling_time,
        "result_time": result_time,
        **results,
    }

    return record


def xml_file_to_dictionary(xml_file):
    "Converts XML file to JSON"
    with open(xml_file, "r") as content_file:
        xml_string = content_file.read()

    return xmltodict.parse(xml_string)


def buoy_xml_to_json(xml_file_path):
    "Converts XML to JSON"
    # convert XML file to a dictionary with matching structure
    data_dict = xml_file_to_dictionary(xml_file_path)

    # parse out a flat dictionary of the data/metadata fields
    record = format_as_flat_record(data_dict)

    # remove fill values
    replace_values(record, "MSNG", None)
    return record


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    """
    Handle command line interaction via click
    """
    record = buoy_xml_to_json(filename)
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
