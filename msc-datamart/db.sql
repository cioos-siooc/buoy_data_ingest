-- Table definition based on variables in https://dd.weather.gc.ca/observations/doc/SWOB-ML_Product_User_Guide_v8.3_e.pdf
-- See section 5.11 OPP Moored Buoy
-- Fields are repeated (eg _1, _2) basd on 'Maximum Multiplicity' field 

-- I left out GRANT commands

--DROP TABLE IF EXISTS swob_marine;
CREATE TABLE swob_marine (
    sampling_time TIMESTAMPTZ,
    result_time TIMESTAMPTZ,
    stn_typ TEXT,
    wmo_synop_id TEXT,
    wmo_identifier_extended NUMERIC,
    stn_nam TEXT,
    msc_id NUMERIC,
    stn_elev NUMERIC,
    sensor_table_number TEXT,
    lat NUMERIC,
    long NUMERIC,
    date_tm TIMESTAMPTZ,
    buoy_typ INT,
    rpt_typ INT,
    crnt_buoy_lat NUMERIC,
    crnt_buoy_lat_qa_summary INT,
    crnt_buoy_lat_data_flag TEXT,
    crnt_buoy_long NUMERIC,
    crnt_buoy_long_qa_summary INT,
    crnt_buoy_long_data_flag TEXT,
    avg_crnt_volt_pst10mts NUMERIC,
    avg_crnt_volt_pst10mts_1 NUMERIC,
    avg_solr_panl_crnt_pst10mts NUMERIC,
    avg_solr_panl_crnt_pst10mts_qa_summary INT,
    avg_solr_panl_crnt_pst10mts_data_flag TEXT,
    avg_solr_panl_crnt_pst10mts_1 NUMERIC,
    avg_solr_panl_crnt_pst10mts_1_qa_summary INT,
    avg_solr_panl_crnt_pst10mts_1_data_flag TEXT,
    avg_batry_volt_pst10mts NUMERIC,
    avg_batry_volt_pst10mts_qa_summary INT,
    avg_batry_volt_pst10mts_data_flag TEXT,
    avg_batry_volt_pst10mts_1 NUMERIC,
    avg_batry_volt_pst10mts_1_qa_summary INT,
    avg_batry_volt_pst10mts_1_data_flag TEXT,
    avg_air_temp_pst10mts NUMERIC,
    avg_air_temp_pst10mts_qa_summary INT,
    avg_air_temp_pst10mts_data_flag TEXT,
    avg_air_temp_pst10mts_1 NUMERIC,
    avg_air_temp_pst10mts_1_qa_summary INT,
    avg_air_temp_pst10mts_1_data_flag TEXT,
    avg_stn_pres_pst10mts NUMERIC,
    avg_stn_pres_pst10mts_qa_summary INT,
    avg_stn_pres_pst10mts_data_flag TEXT,
    avg_stn_pres_pst10mts_1 NUMERIC,
    avg_stn_pres_pst10mts_1_qa_summary INT,
    avg_stn_pres_pst10mts_1_data_flag TEXT,
    avg_stn_pres_pst10mts_2 NUMERIC,
    avg_stn_pres_pst10mts_2_qa_summary INT,
    avg_stn_pres_pst10mts_2_data_flag TEXT,
    avg_sea_sfc_temp_pst10mts NUMERIC,
    avg_sea_sfc_temp_pst10mts_qa_summary INT,
    avg_sea_sfc_temp_pst10mts_data_flag TEXT,
    avg_sea_sfc_temp_pst10mts_1 NUMERIC,
    avg_sea_sfc_temp_pst10mts_1_qa_summary INT,
    avg_sea_sfc_temp_pst10mts_1_data_flag TEXT,
    avg_wnd_spd_pst10mts NUMERIC,
    avg_wnd_spd_pst10mts_qa_summary INT,
    avg_wnd_spd_pst10mts_data_flag TEXT,
    avg_wnd_spd_pst10mts_1 NUMERIC,
    avg_wnd_spd_pst10mts_1_qa_summary INT,
    avg_wnd_spd_pst10mts_1_data_flag TEXT,
    avg_wnd_spd_pst10mts_2 NUMERIC,
    avg_wnd_spd_pst10mts_2_qa_summary INT,
    avg_wnd_spd_pst10mts_2_data_flag TEXT,
    avg_wnd_dir_pst10mts NUMERIC,
    avg_wnd_dir_pst10mts_qa_summary INT,
    avg_wnd_dir_pst10mts_data_flag TEXT,
    avg_wnd_dir_pst10mts_1 NUMERIC,
    avg_wnd_dir_pst10mts_1_qa_summary INT,
    avg_wnd_dir_pst10mts_1_data_flag TEXT,
    avg_wnd_dir_pst10mts_2 NUMERIC,
    avg_wnd_dir_pst10mts_2_qa_summary INT,
    avg_wnd_dir_pst10mts_2_data_flag TEXT,
    max_avg_wnd_spd_pst10mts NUMERIC,
    max_avg_wnd_spd_pst10mts_qa_summary INT,
    max_avg_wnd_spd_pst10mts_data_flag TEXT,
    max_avg_wnd_spd_pst10mts_1 NUMERIC,
    max_avg_wnd_spd_pst10mts_1_qa_summary INT,
    max_avg_wnd_spd_pst10mts_1_data_flag TEXT,
    max_avg_wnd_spd_pst10mts_2 NUMERIC,
    max_avg_wnd_spd_pst10mts_2_qa_summary INT,
    max_avg_wnd_spd_pst10mts_2_data_flag TEXT,
    wnd_snsr_vert_disp NUMERIC,
    wnd_snsr_vert_disp_qa_summary INT,
    wnd_snsr_vert_disp_data_flag TEXT,
    wnd_snsr_vert_disp_1 NUMERIC,
    wnd_snsr_vert_disp_1_qa_summary INT,
    wnd_snsr_vert_disp_1_data_flag TEXT,
    wnd_snsr_vert_disp_2 NUMERIC,
    wnd_snsr_vert_disp_2_qa_summary INT,
    wnd_snsr_vert_disp_2_data_flag TEXT,
    pk_wave_pd_pst20mts NUMERIC,
    pk_wave_pd_pst20mts_qa_summary INT,
    pk_wave_pd_pst20mts_data_flag TEXT,
    pk_wave_pd_pst20mts_1 NUMERIC,
    pk_wave_pd_pst20mts_1_qa_summary INT,
    pk_wave_pd_pst20mts_1_data_flag TEXT,
    pk_wave_hgt_pst20mts NUMERIC,
    pk_wave_hgt_pst20mts_qa_summary INT,
    pk_wave_hgt_pst20mts_data_flag TEXT,
    pk_wave_hgt_pst20mts_1 NUMERIC,
    pk_wave_hgt_pst20mts_1_qa_summary INT,
    pk_wave_hgt_pst20mts_1_data_flag TEXT,
    sig_wave_pd_pst20mts NUMERIC,
    sig_wave_pd_pst20mts_qa_summary INT,
    sig_wave_pd_pst20mts_data_flag TEXT,
    sig_wave_pd_pst20mts_1 NUMERIC,
    sig_wave_pd_pst20mts_1_qa_summary INT,
    sig_wave_pd_pst20mts_1_data_flag TEXT,
    sig_wave_hgt_pst20mts NUMERIC,
    sig_wave_hgt_pst20mts_qa_summary INT,
    sig_wave_hgt_pst20mts_data_flag TEXT,
    sig_wave_hgt_pst20mts_1 NUMERIC,
    sig_wave_hgt_pst20mts_1_qa_summary INT,
    sig_wave_hgt_pst20mts_1_data_flag TEXT,
    avg_wave_pd_pst20mts NUMERIC,
    avg_wave_pd_pst20mts_qa_summary INT,
    avg_wave_pd_pst20mts_data_flag TEXT,
    avg_wave_pd_pst20mts_1 NUMERIC,
    avg_wave_pd_pst20mts_1_qa_summary INT,
    avg_wave_pd_pst20mts_1_data_flag TEXT,
    avg_wave_hgt_pst20mts NUMERIC,
    avg_wave_hgt_pst20mts_qa_summary INT,
    avg_wave_hgt_pst20mts_data_flag TEXT,
    avg_wave_hgt_pst20mts_1 NUMERIC,
    avg_wave_hgt_pst20mts_1_qa_summary INT,
    avg_wave_hgt_pst20mts_1_data_flag TEXT,
    avg_max_wave_pd_pst20mts NUMERIC,
    avg_max_wave_pd_pst20mts_qa_summary INT,
    avg_max_wave_pd_pst20mts_data_flag TEXT,
    avg_max_wave_pd_pst20mts_1 NUMERIC,
    avg_max_wave_pd_pst20mts_1_qa_summary INT,
    avg_max_wave_pd_pst20mts_1_data_flag TEXT,
    avg_max_wave_hgt_pst20mts NUMERIC,
    avg_max_wave_hgt_pst20mts_qa_summary INT,
    avg_max_wave_hgt_pst20mts_data_flag TEXT,
    avg_max_wave_hgt_pst20mts_1 NUMERIC,
    avg_max_wave_hgt_pst20mts_1_qa_summary INT,
    avg_max_wave_hgt_pst20mts_1_data_flag TEXT,
    avg_mslp_pst10mts NUMERIC,
    avg_mslp_pst10mts_qa_summary INT,
    avg_mslp_pst10mts_data_flag TEXT,
    avg_mslp_pst10mts_1 NUMERIC,
    avg_mslp_pst10mts_1_qa_summary INT,
    avg_mslp_pst10mts_1_data_flag TEXT,
    avg_wtr_lvl_snsr_volt_pst10mts NUMERIC,
    avg_wtr_lvl_snsr_volt_pst10mts_qa_summary INT,
    avg_wtr_lvl_snsr_volt_pst10mts_data_flag TEXT,
    avg_wtr_lvl_snsr_volt_pst10mts_1 NUMERIC,
    avg_wtr_lvl_snsr_volt_pst10mts_1_qa_summary INT,
    avg_wtr_lvl_snsr_volt_pst10mts_1_data_flag TEXT,
    pres_tend_amt_pst3hrs NUMERIC,
    pres_tend_amt_pst3hrs_qa_summary INT,
    pres_tend_amt_pst3hrs_data_flag TEXT,
    pres_tend_amt_pst3hrs_1 NUMERIC,
    pres_tend_amt_pst3hrs_1_qa_summary INT,
    pres_tend_amt_pst3hrs_1_data_flag TEXT,
    pres_tend_char_pst3hrs INT,
    pres_tend_char_pst3hrs_qa_summary INT,
    pres_tend_char_pst3hrs_data_flag TEXT,
    UNIQUE(sampling_time, wmo_synop_id)
  );

-- Dispaly last month in ERDDAP, or adjust as needed

-- DROP VIEW IF EXISTS swob_marine_view
CREATE OR REPLACE VIEW swob_marine_view AS
  SELECT * FROM swob_marine WHERE sampling_time > ( NOW() - INTERVAL '1 month' );