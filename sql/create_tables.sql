CREATE TABLE IF NOT EXISTS weather_daily (
    weather_date DATE PRIMARY KEY,
    temperature_2m_max NUMERIC,
    temperature_2m_min NUMERIC,
    temperature_2m_mean NUMERIC,
    precipitation_sum NUMERIC,
    wind_speed_10m_max NUMERIC,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);