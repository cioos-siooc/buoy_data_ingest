# MEDS Buoy data ingestion tool

## Installation

This tool helps download buoy data in CSV format from MEDS.

1. Edit buoys_download.txt to the buoys you want to include in your dataset. See list of buoys [here](http://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/INVENTORY/b_pw_inv.html)
2. (Optional) Edit the zip file or csv file download locations in `meds_download.sh`
3. Run `sh meds_download.sh`, and put it a crontab to run daily
4. Edit the datasets.xml snippet to match the CSV directory set in `meds_download` script. Merge this XML snippet into your ERDDAP installation.

## Running on OSX

- in `meds_download.sh`, Change `sed` to `gsed` for running on OSX

## Links

http://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/INVENTORY/b_pw_inv.html

http://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/csvData
