#!/usr/bin/env python

"""

Small script to fix up MEDS data CSV files:
 - change dates to ISO 8601 and records with invalid datetimes (eg "01/10/1988 00:84")
 - set fixed lat/lon based on most recent metadata for each buoy
 - set fixed columns for all files

This files replaces "csv_combine.py" which was used previously.

Takes ~5 minutes to run

"""

import glob

import pandas as pd
import requests


def get_deployment_metadata():
    url = "https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/INVENTORY/b_pw_inv.json"

    res = requests.get(url).json()["data"]

    df = pd.DataFrame(
        res,
        columns=[
            "station_name",
            "station",
            "type",
            "date_start",
            "date_end",
            "lat",
            "lon",
            "depth",
            "days",
        ],
    ).set_index("station", drop=False)

    df["date_start"] = pd.to_datetime(df.date_start).dt.tz_localize(None)
    df["date_end"] = pd.to_datetime(df.date_end).dt.tz_localize(None)

    # when there are multiple deployments, just get the most recent one
    df = df.sort_values(by="date_end").drop_duplicates("station", keep="last")

    return df


def fix_csv_files(input_folder, output_folder):
    """
    Fixes csv files
    """

    df_metadata = get_deployment_metadata()

    # some files have fewer columns, this ensures they all have the same columns and order for loading into the DB
    column_order = [
        "STN_ID",
        "DATE",
        "Q_FLAG",
        "LATITUDE",
        "LONGITUDE",
        "DEPTH",
        "VCAR",
        "VTPK",
        "VWH",
        "VCMX",
        "VTP",
        "WDIR",
        "WSPD",
        "WSS",
        "GSPD",
        "WDIR_2",
        "WSPD_2",
        "WSS_2",
        "GSPD_2",
        "ATMS",
        "ATMS_2",
        "DRYT",
        "SSTP",
        "preciseLat",
        "preciseLon",
    ]

    df_cols = pd.DataFrame(columns=column_order)
    for file in glob.glob(input_folder + "/*.csv"):
        print(file)

        station = str(file)[6:-4].upper()
        df = pd.read_csv(
            file, parse_dates=True, dtype=str
        )

        num_coordinates = len(df[["LATITUDE", "LONGITUDE"]].drop_duplicates())

        # correct longitude
        df["LONGITUDE"] = -df["LONGITUDE"].astype("double")
        df["preciseLat"] = df["LATITUDE"]
        df["preciseLon"] = df["LONGITUDE"]

        if station in df_metadata.index:
            df["LATITUDE"] = df_metadata.loc[station]["lat"]
            df["LONGITUDE"] = df_metadata.loc[station]["lon"]
        elif num_coordinates == 1:
            print("single coordinate station without metadata")
            df["LATITUDE"] = df["LATITUDE"]
            # this file only has one coordinate, so precise can be set to lat/lon
            pass
        else:
            # more than one coordinate in file and no deployment data, this shouldnt happen
            print("Missing metadata for station,", station, ". Skipping.")
            continue

        # remove bad dates, eg "01/10/1988 00:84"
        df["DATE"] = pd.to_datetime(df.DATE, errors="coerce").dt.tz_localize(None)
        df = df.query("DATE.isna()==False")

        # I dont know why this is needed or if it is anymore
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        # make sure all the same columns exist in each file
        df_out = pd.concat([df, df_cols], ignore_index=True)

        # set consistent column order
        df_out = df_out[column_order]
        outfile = output_folder + "/" + station + "-fixed.csv"
        print("Wrote ", outfile)
        df_out.to_csv(outfile, index=False)


input_folder = "./csv"
output_folder = "./csv-fixed"

fix_csv_files(input_folder, output_folder)
