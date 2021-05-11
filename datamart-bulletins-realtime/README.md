# Realtime Moored Buoy ingestion tool

MEDS buoy data can be read in realtime from <https://dd.weather.gc.ca/observations/>. This is for the non-OPP buoys, see the 'msc-datamart' folder for the OPP buoys.

This package:

- subscribes the the AMQP realtime stream using [Sarracenia](https://github.com/MetPX/sarracenia)
- parses the FM13 messages using [metaf2xml](https://metaf2xml.sourceforge.io/)
- inserts a record into a Postgres database
- includes an entry for datasets.xml so it can be streamed into [ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap)

## Installation

1. `cd` to this directory
1. Download [metaf2xml](https://metaf2xml.sourceforge.io/), install parser, make sure it works by running `perl /opt/metaf2xml-2.6/bin/metaf2xml.pl -h`.
1. Install a Python3 virtualenv
1. Install this package using -e

   ```bash
   pip install -e .
   ```

1. Edit the DB connection information in fm13_ingest/ingest_to_db.py
1. Edit fm13.conf to include the regions/messages you would like
1. Setup a DB to connect to, use db.sql to create a table & view

## Running

1. `cd` to this directory
1. Activate your Python3 virtualenv
1. Test that the packages are installed:

   ```bash
   python -m fm13_ingest --level decode sample_fm13
   ```

1. Test database connection

   ```bash
   python -m fm13_ingest --level ingest sample_fm13
   ```

1. Start service

   ```bash
   sr_subscribe start fm13.conf
   ```
