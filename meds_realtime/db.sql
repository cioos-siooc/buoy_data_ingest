-- TODO get date in here
DROP TABLE IF EXISTS meds_buoys_realtime_non_opp;
CREATE TABLE meds_buoys_realtime_non_opp (
    station_id NUMERIC NOT NULL,
    result_time TIMESTAMPTZ,
    air_temperature NUMERIC,
    office TEXT,
    headers JSONB,
    highest_mean_speed_wind NUMERIC,
    lat NUMERIC,
    lon NUMERIC,
    precip NUMERIC,
    pressure NUMERIC,
    pressure_change NUMERIC,
    pressure_tendency NUMERIC,
    sea_surface_temp NUMERIC,
    station_region TEXT,
    water_temp_sal_measurement NUMERIC,
    wave_height NUMERIC,
    wave_period NUMERIC,
    wind_dir NUMERIC,
    wind_measurement_period NUMERIC,
    wind_speed NUMERIC,
    wx_ind_val NUMERIC,
    UNIQUE(station_id,result_time)
);


-- DROP VIEW IF EXISTS swob_marine_view
CREATE OR REPLACE VIEW meds_buoys_realtime_non_opp_view AS
  SELECT * FROM meds_buoys_realtime_non_opp WHERE result_time > ( NOW() - INTERVAL '1 month' );

