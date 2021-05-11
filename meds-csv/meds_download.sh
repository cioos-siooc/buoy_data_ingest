#!/bin/sh

#
# Download and extracts CSV zips from MEDS. Only downloads when a newer zip file is available.
#
# Run: sh meds_download.sh /path/to/csvs
#
#

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)" # set folder to save ZIPs

zip_folder=$DIR/zip

# set folder to save CSVs, defaults to 'csv'
if [ -z "$1" ]; then
   csv_folder="csv"
else
   csv_folder="$1"
fi

# set file with lis of buoys
buoy_file=$DIR/buoys_download.txt

while read -r p; do
   wget -q --restrict-file-names=lowercase -N --ignore-case --directory-prefix $zip_folder "http://meds-sdmm.dfo-mpo.gc.ca/alphapro/wave/waveshare/csvData/${p}_csv.zip"
   # sleep 1
done <$buoy_file

# extract to lower case, only extract if file has changed
unzip -qq -LL -o "$zip_folder/*_csv.zip" -d $csv_folder

echo "Fixing up CSV headers.."

# Remove trailing comma from first line of each file
sed -i "1,1s/,\W*$//" $csv_folder/*.csv

# Columns ATMS,GSPD,WSPD,WDIR are duplicated so I added '2'
# set this as the new header
sed -i "1c\STN_ID,DATE,Q_FLAG,LATITUDE,LONGITUDE,DEPTH,VCAR,VTPK,VWH\$,VCMX,VTP\$,WDIR,WSPD,WSS\$,GSPD,WDIR2,WSPD2,WSS\$2,GSPD2,ATMS,ATMS2,DRYT,SSTP" $csv_folder/c*.csv

chmod 644 -R $csv_folder/*

echo "Done"
