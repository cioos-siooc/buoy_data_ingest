# ECCC / DFO Buoy ingestion tools

This package harvests buoy data from ECCC/DFO and has steps to put the data into [ERDDAP](https://data.cioospacific.ca/erddap). Click on a folder for a more in-depth README.

## Datamart Bulletins Realtime

- Realtime bulletins from datamart alphanumeric. Buoy data is parsed from the raw FM13 format and formatted. MSC Datamart AMQP -> Postgres DB -> ERDDAP

## Datamart SWOB Marine Realtime

- Realtime OPP moored buoy data from MSC Datamart. MSC Datamart AMQP -> Postgres DB -> ERDDAP

## MEDS-CSV

- Scripts to download non-realtime CSV data
