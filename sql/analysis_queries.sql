-- 1. Preview the weather table
SELECT *
FROM weather_daily
LIMIT 10;


-- 2. Confirm total number of rows
SELECT COUNT(*) AS total_rows
FROM weather_daily;


-- 3. Basic weather summary
SELECT
    ROUND(AVG(temperature_2m_mean), 2) AS avg_temp,
    ROUND(AVG(temperature_2m_max), 2) AS avg_high,
    ROUND(AVG(temperature_2m_min), 2) AS avg_low,
    ROUND(SUM(precipitation_sum), 2) AS total_precipitation,
    ROUND(AVG(wind_speed_10m_max), 2) AS avg_max_wind_speed
FROM weather_daily;


-- 4. Ten hottest days
SELECT
    weather_date,
    temperature_2m_max
FROM weather_daily
ORDER BY temperature_2m_max DESC
LIMIT 10;


-- 5. Ten coldest days
SELECT
    weather_date,
    temperature_2m_min
FROM weather_daily
ORDER BY temperature_2m_min ASC
LIMIT 10;


-- 6. Ten wettest days
SELECT
    weather_date,
    precipitation_sum
FROM weather_daily
ORDER BY precipitation_sum DESC
LIMIT 10;


-- 7. Monthly weather summary
SELECT
    DATE_TRUNC('month', weather_date)::date AS month,
    ROUND(AVG(temperature_2m_mean), 2) AS avg_monthly_temp,
    ROUND(AVG(temperature_2m_max), 2) AS avg_monthly_high,
    ROUND(AVG(temperature_2m_min), 2) AS avg_monthly_low,
    ROUND(SUM(precipitation_sum), 2) AS monthly_precipitation,
    ROUND(AVG(wind_speed_10m_max), 2) AS avg_max_wind_speed
FROM weather_daily
GROUP BY DATE_TRUNC('month', weather_date)
ORDER BY month;


-- 8. Seven-day moving average temperature
SELECT
    weather_date,
    temperature_2m_mean,
    ROUND(
        AVG(temperature_2m_mean) OVER (
            ORDER BY weather_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS seven_day_moving_avg_temp
FROM weather_daily
ORDER BY weather_date;


-- 9. Rank days by maximum temperature
SELECT
    weather_date,
    temperature_2m_max,
    RANK() OVER (
        ORDER BY temperature_2m_max DESC
    ) AS heat_rank
FROM weather_daily
ORDER BY heat_rank
LIMIT 20;


-- 10. Compare each day to the previous day
SELECT
    weather_date,
    temperature_2m_mean,
    LAG(temperature_2m_mean) OVER (
        ORDER BY weather_date
    ) AS previous_day_temp,
    ROUND(
        temperature_2m_mean - LAG(temperature_2m_mean) OVER (
            ORDER BY weather_date
        ),
        2
    ) AS temp_change_from_previous_day
FROM weather_daily
ORDER BY weather_date;