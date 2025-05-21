with raw as (
    select * from {{ source('weather_schema', 'weather_raw') }}
)

select
    city,
    temperature,
    humidity,
    weather,
    timestamp as recorded_at
from raw
