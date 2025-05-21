select
    city,
    avg(temperature) as avg_temp,
    max(humidity) as max_humidity,
    count(*) as readings_count
from {{ ref('stg_weather_raw') }}
group by city
