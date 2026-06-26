import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


PROCESSED_DATA_PATH = Path("data/processed/weather_daily.csv")


def get_database_engine():
    """Create a SQLAlchemy engine for PostgreSQL."""

    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection_string = (
        f"postgresql+psycopg2://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    return create_engine(connection_string)


def load_weather_data(path: Path) -> None:
    """Load processed weather data into PostgreSQL."""

    df = pd.read_csv(path)
    engine = get_database_engine()

    with engine.begin() as connection:
        connection.execute(text("DELETE FROM weather_daily;"))

    df.to_sql(
        name="weather_daily",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(f"Loaded {len(df)} rows into weather_daily.")


def main() -> None:
    load_weather_data(PROCESSED_DATA_PATH)


if __name__ == "__main__":
    main()