"""imports"""
from pyspark.sql import DataFrame

from weather.common.reader import create_df_with_schema, read_from_parquet
from weather.data.real_time_weather.real_time_weather_schema import (
    real_time_weather_SCHEMA,
)


class maag_master_agrem_Reader:
    """tab init path"""
    def __init__(self, path: str) -> None:

        self.path = path

    def read(self) -> DataFrame:
        """tab reader"""
        real_time_weather_df: DataFrame = read_from_parquet(
            self.path
        ).select(*real_time_weather_SCHEMA.fieldNames())

        return create_df_with_schema(
            real_time_weather_df,
            real_time_weather_SCHEMA,
        )
