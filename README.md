# ECCC / DFO Buoy ingestion tools

This pacakage harvests marine buoy data from ECCC/DFO and has steps to put the data into [ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap). Click on a folder for more in depth READMEs.

## MSC-Datamart

- Realtime OPP moored buoy data from MSC Datamart via AMPQ -> Postgres DB -> ERDDAP

## MEDS

- Non-realtime data is harvested from .csv files -> ERDDAP

## MEDS Realtime

- Realtime non-OPP moored buoy data from Datamart in FM13 format via AMPQ -> Postgres DB -> ERDDAP
