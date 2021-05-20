# SWOB-Marine Ingestion Tools

This repo contains scripts to receive and parse the realtime marine [SWOB-XML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/SWOB-ML_Product_User_Guide_v8.3_e.pdf) stream from [MSC Datamart](https://dd.weather.gc.ca/observations/swob-ml/marine/moored-buoys/) and put it into a database. It receives data using the AMQP system described [here](https://eccc-msc.github.io/open-data/msc-datamart/amqp_en/) . Also includes [ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/index.html) config to get it from the database into ERDDAP.

## Installation

1. `cd` into this directory

1. If needed, install virtualenv.

   `pip install virtualenv --user`

1. Create and activate new virtual environment

   ```sh
      virtualenv -p python3 venv
      source venv/bin/activate
   ```

1. Install the buoy loading script with

   `pip install -e .`

1. Test that the package is installed by running `python -m msc_ingest.parse_xml sample_records/sample.xml` from this directory

1. Edit dd_swob_marine.conf as needed, eg to change temp directory

1. Create a postgres database and run `db.sql` to create a table, and GRANT permissions to a user to read/write

1. Change `config.ini` to reflect your DB settings.

1. Test that it works by running `python msc_ingest/ingest_to_db.py sample_records/sample.xml` from this directory. This should create a new record in your table. Note that running this multiple times will not produce multiple records.

1. Start recording data to the database with
   `sr_subscribe start dd_swob_marine.conf`

## Just parsing an XML file

After installing,

```sh
python -m msc_ingest.parse_xml sample_records/sample.xml
```

## ERDDAP

The datasets.xml provided should cover all of the possible fields in the data, based on the

## Troubleshooting

Sarracenia logging:
`sr_subscribe log dd_swob_marine.conf`

## Buoy list

At time of writing there are 3 Atlantic and 2 Pacific buoys available in this system:

Pacific:
46303
46304

Atlantic:
44488
44489
44490

## Links

MSC Datamart Documentation
<https://dd.weather.gc.ca/observations/doc/>

Sarracenia
<https://github.com/MetPX/sarracenia>

Raw XML files that get pushed into this system. Also find list of currently published buoys here
<https://dd.weather.gc.ca/observations/swob-ml/marine/moored-buoys>

SWOB Manual
<https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_station/SWOB-ML_Product_User_Guide_v8.3_e.pdf>
