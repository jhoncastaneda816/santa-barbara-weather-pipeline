import json
from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/weather_raw.json")
PROCESSED_DATA_PATH = Path("data/processed/weather_daily.csv")


def read_raw_json(path: Path) -> dict:
    """Read raw JSON data."""

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    """Convert raw Open-Meteo JSON into a clean daily weather table."""

    daily_data = raw_data["daily"]

    df = pd.DataFrame(
        {
            "weather_date": daily_data["time"],
            "temperature_2m_max": daily_data["temperature_2m_max"],
            "temperature_2m_min": daily_data["temperature_2m_min"],
            "temperature_2m_mean": daily_data["temperature_2m_mean"],
            "precipitation_sum": daily_data["precipitation_sum"],
            "wind_speed_10m_max": daily_data["wind_speed_10m_max"],
        }
    )

    df["weather_date"] = pd.to_datetime(df["weather_date"]).dt.date

    return df


def save_processed_data(df: pd.DataFrame, path: Path) -> None:
    """Save cleaned weather data as CSV."""

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main() -> None:
    raw_data = read_raw_json(RAW_DATA_PATH)
    weather_df = transform_weather_data(raw_data)
    save_processed_data(weather_df, PROCESSED_DATA_PATH)

    print(f"Processed weather data saved to {PROCESSED_DATA_PATH}")
    print(weather_df.head())


if __name__ == "__main__":
    main()