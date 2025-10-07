# first do source activate venv/bin/activate
source /home/cioos/buoy_data_ingest/msc-datamart/venv/bin/activate
cd /home/cioos/buoy_data_ingest/msc-datamart
sr_subscribe restart /home/cioos/buoy_data_ingest/msc-datamart/dd_swob_marine.conf
