import json
from pathlib import Path

import requests


RAW_DATA_PATH = Path("data/raw/weather_raw.json")


def fetch_weather_data() -> dict:
    """Fetch historical daily weather data for Santa Barbara from Open-Meteo."""

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 34.4208,
        "longitude": -119.6982,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "precipitation_sum",
            "wind_speed_10m_max",
        ],
        "timezone": "America/Los_Angeles",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


def save_raw_data(data: dict, path: Path) -> None:
    """Save raw API response as JSON."""

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main() -> None:
    weather_data = fetch_weather_data()
    save_raw_data(weather_data, RAW_DATA_PATH)
    print(f"Raw weather data saved to {RAW_DATA_PATH}")


if __name__ == "__main__":
    main()