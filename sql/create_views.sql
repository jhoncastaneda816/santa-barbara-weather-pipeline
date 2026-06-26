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