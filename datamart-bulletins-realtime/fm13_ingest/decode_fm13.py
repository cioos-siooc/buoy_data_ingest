#!/usr/bin/env python3

import subprocess
from benedict import benedict
import xmltodict
from dotenv import dotenv_values


"""
This file has funcions to convert the  FM13 text into JSON using the
metaf2xml perl package

Example of FM13 input:

SNVD17 CWVR 011900
BBXX
46185 01191 99524 71298 46/// // /00 10094 40123 57011
22200 00084 10402 70012 333 91201=

decoding steps:
 - First line is ignored
 - last '=' is removed
 - newlines replaced by space
 - metaf2xml converts it to XML
 - xmltodict converts it to dict
 - remapped to a flat dict with remapDict()
"""
config = dotenv_values("config.ini")

METAF2XML_PATH = config['METAF2XML_PATH']


def parse(data, path):
    """select JSON path in dict or return None if path doesnt exist"""
    parsed = benedict(data)
    try:
        return parsed[path]
    except KeyError:
        return None


def remap_dict(data: dict) -> dict:
    """
    Remapped to flat dict. Keys match DB table column names
    """
    return {
        "pressure": parse(data, "SLP.pressure.v"),
        # "baseLowestCloud": parse(data, 'baseLowestCloud.v'),
        "station_id": parse(data, "callSign.id.v"),
        "station_region": parse(data, "callSign.region.v"),
        # "stationType": parse(data, 'obsStationType.stationType.v'),
        "day": parse(data, "obsTime.timeAt.day.v"),
        "hour": parse(data, "obsTime.timeAt.hour.v"),
        "precip": parse(data, "precipInd.precipIndVal.v"),
        "pressure_change": parse(data, "pressureChange.pressureChangeVal.v"),
        "pressure_tendency": parse(data, "pressureChange.pressureTendency.v"),
        # "pressureChangeHoursBeforeObs": parse(data, 'pressureChange.timeBeforeObs.hours.v'),
        # "reportModifier": parse(data, 'reportModifier.modifierType.v'),
        "wind_measurement_period": parse(data, "sfcWind.measurePeriod.v"),
        "wind_dir": parse(data, "sfcWind.wind.dir.v"),
        "wind_speed": parse(data, "sfcWind.wind.speed.v"),
        "lat": parse(data, "stationPosition.lat.v"),
        "lon": parse(data, "stationPosition.lon.v"),
        # "station_level_pressure": parse(data, 'stationPressure.pressure.v'),
        # "isStationary": parse(data,
        #                       'synop_section2.displacement.isStationary'),
        # "synop2TimeBeforeObsHours": parse(data, 'synop_section2.displacement.timeBeforeObs.hours.v'),
        "sea_surface_temp": parse(data, "synop_section2.seaSurfaceTemp.temp.v"),
        "water_temp_sal_measurement": parse(
            data, "synop_section2.seaSurfaceTemp.waterTempSalMeasurement.v"
        ),
        "wave_height": parse(data, "synop_section2.waves.height.v"),
        "wave_period": parse(data, "synop_section2.waves.wavePeriod.v"),
        # "highestMeanSpeedHoursBefore": parse(data, 'synop_section3.highestMeanSpeed.timeBeforeObs.hours.v'),
        "highest_mean_speed_wind": parse(
            data, "synop_section3.highestMeanSpeed.wind.speed.v"
        ),
        "air_temperature": parse(data, "temperature.air.temp.v"),
        "wx_ind_val": parse(data, "wxInd.wxIndVal.v"),
    }


def decode(text: str) -> dict:
    """Turns FM-13 text into a dictionary"""
    lines = text.splitlines()
    newinput = ((" ".join(lines[1:])).replace("\n", "").strip("=")).strip()
    xml = subprocess.check_output(
        ["perl", METAF2XML_PATH, "-f", "-", "-o", "-", f"{newinput}"]
    )

    res = xmltodict.parse(str(xml.decode()), attr_prefix="")
    flat_dict = remap_dict(res["data"]["reports"]["synop"])
    return flat_dict
