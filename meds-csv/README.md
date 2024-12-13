# MEDS Buoy data ingestion tool

## Installation

This tool helps download buoy data in CSV format from MEDS.

1. Create and activate new virtual environment

   ```sh
      virtualenv -p python3 venv
      source venv/bin/activate
   ```

1. Run `pip install -e ./meds_csv_fix`
1. Run `sh meds_download.sh`

## Running on OSX

- in `meds_download.sh`, Change `sed` to `gsed` for running on OSX

## Links

http://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/INVENTORY/b_pw_inv.html

http://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/csvData
