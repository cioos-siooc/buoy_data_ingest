#!/bin/sh

# Download and extracts CSV zips from MEDS. Only downloads when a newer zip file is available.

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)" # set folder to save ZIPs

zip_folder=$DIR/zip

# set folder to save CSVs
csv_folder=$DIR/csv
combined_csv_path="/home/cioos/buoy_qc_operationalize/src/meds_csv.csv"

echo "Downloading MEDS data.."
url="https://www.meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/CSVDATA/"
wget -r -np -nd -qq --restrict-file-names=lowercase -N --ignore-case --directory-prefix $zip_folder "${url}"

# extract to lower case, only extract if file has changed
# ||true lets it skip a bad zip file
echo "Unzipping.."
unzip -qq -LL -o "$zip_folder/*_csv.zip" -d $csv_folder || true

echo "Fixing up CSV headers.."

# Remove trailing comma from first line of each file
# use gsed on OSX
sed -i "1,1s/,\W*$//" $csv_folder/*.csv

# Headers in files starting with 'c':
# Columns ATMS,GSPD,WSPD,WDIR are duplicated so I added '2'
# STN_ID,DATE,Q_FLAG,LATITUDE,LONGITUDE,DEPTH,VCAR,VTPK,VWH$,VCMX,VTP$,WDIR,WSPD,WSS$,GSPD,WDIR,WSPD,WSS$,GSPD,ATMS,ATMS,DRYT,SSTP,

# Headers in other files:
# STN_ID,DATE,Q_FLAG,LATITUDE,LONGITUDE,DEPTH,VCAR,VTPK,

# cant just change all headers as there would be missing commas in data
# use gsed on OSX
sed -i "1c\STN_ID,DATE,Q_FLAG,LATITUDE,LONGITUDE,DEPTH,VCAR,VTPK,VWH,VCMX,VTP,WDIR,WSPD,WSS,GSPD,WDIR_2,WSPD_2,WSS_2,GSPD_2,ATMS,ATMS_2,DRYT,SSTP" $csv_folder/c*.csv

chmod -R 644 $csv_folder/*

echo "Fixing up CSV data. This takes a while"
python3 meds-csv-fix.py >/dev/null

echo "Combining all CSVs into one big one"
awk '(NR == 1) || (FNR > 1)' ./csv-fixed/*-fixed.csv >$combined_csv_path

echo "Done"
