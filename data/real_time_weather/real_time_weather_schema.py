"""imports"""

from pyspark.sql.types import FloatType, StringType, StructField, StructType

CURRENT_AIR_QUALITY: str = "current_air_quality"
CURRENT_CLOUD: float = "current_cloud"
CURRENT_CONDITION_CODE: float = "current_condition_code"
CURRENT_CONDITION_ICON: str = "current_condition_icon"
CURRENT_CONDITION_TEXT: str = "current_condition_text"
CURRENT_FEELSLIKE_C: float = "current_feelslike_c"
CURRENT_FEELSLIKE_F: float = "current_feelslike_f"
CURRENT_GUST_KPH: float = "current_gust_kph"
CURRENT_GUST_MPH: float = "current_gust_mph"
CURRENT_HUMIDITY: float = "current_humidity"
CURRENT_IS_DAY: float = "current_is_day"
CURRENT_LAST_UPDATED: str = "current_last_updated"
CURRENT_LAST_UPDATED_EPOCH: float = "current_last_updated_epoch"
CURRENT_PRECIP_IN: float = "current_precip_in"
CURRENT_PRECIP_MM: float = "current_precip_mm"
CURRENT_PRESSURE_IN: float = "current_pressure_in"
CURRENT_PRESSURE_MM: float = "current_pressure_mm"
CURRENT_TEMP_C: float = "current_temp_c"
CURRENT_TEMP_F: float = "current_temp_f"
CURRENT_UV: float = "current_uv"
CURRENT_VIS_KM: float = "current_vis_km"
CURRENT_VIS_MILES: float = "current_vis_miles"
CURRENT_WIND_DEGREE: float = "current_wind_degree"
CURRENT_WIND_DIR: str = "current_wind_dir"
CURRENT_WIND_KPH: float = "current_wind_kph"
CURRENT_WIND_MPH: float = "current_wind_mph"
LOCATION_COUNTRY: str = "location_country"
LOCATION_LAT: float = "location_lat"
LOCATION_LOCALTIME: str = "location_localtime"
LOCATION_LOCALTIME_EPOCH: float = "location_localtime_epoch"
LOCATION_LON: float = "location_lon"
LOCATION_NAME: str = "location_name"
LOCATION_REGION: str = "location_region"
LOCATION_TZ_ID: str = "location_tz_id"


real_time_weather_SCHEMA: StructType = StructType ([
    StructField(CURRENT_AIR_QUALITY, StringType(), True),
    StructField(CURRENT_CLOUD, FloatType(), True),
    StructField(CURRENT_CONDITION_CODE, FloatType(), True),
    StructField(CURRENT_CONDITION_ICON, StringType(), True),
    StructField(CURRENT_CONDITION_TEXT, StringType(), True),
    StructField(CURRENT_FEELSLIKE_C, FloatType(), True),
    StructField(CURRENT_FEELSLIKE_F, FloatType(), True),
    StructField(CURRENT_GUST_KPH, FloatType(), True),
    StructField(CURRENT_GUST_MPH, FloatType(), True),
    StructField(CURRENT_HUMIDITY, FloatType(), True),
    StructField(CURRENT_IS_DAY, FloatType(), True),
    StructField(CURRENT_LAST_UPDATED, StringType(), True),
    StructField(CURRENT_LAST_UPDATED_EPOCH, FloatType(), True),
    StructField(CURRENT_PRECIP_IN, FloatType(), True),
    StructField(CURRENT_PRECIP_MM, FloatType(), True),
    StructField(CURRENT_PRESSURE_IN, FloatType(), True),
    StructField(CURRENT_PRESSURE_MM, FloatType(), True),
    StructField(CURRENT_TEMP_C, FloatType(), True),
    StructField(CURRENT_TEMP_F, FloatType(), True),
    StructField(CURRENT_UV, FloatType(), True),
    StructField(CURRENT_VIS_KM, FloatType(), True),
    StructField(CURRENT_VIS_MILES, FloatType(), True),
    StructField(CURRENT_WIND_DEGREE, FloatType(), True),
    StructField(CURRENT_WIND_DIR, StringType(), True),
    StructField(CURRENT_WIND_KPH, FloatType(), True),
    StructField(CURRENT_WIND_MPH, FloatType(), True),
    StructField(LOCATION_COUNTRY, StringType(), True),
    StructField(LOCATION_LAT, FloatType(), True),
    StructField(LOCATION_LOCALTIME, StringType(), True),
    StructField(LOCATION_LOCALTIME_EPOCH, FloatType(), True),
    StructField(LOCATION_LON, FloatType(), True),
    StructField(LOCATION_NAME, StringType(), True),
    StructField(LOCATION_REGION, StringType(), True),
    StructField(LOCATION_TZ_ID, StringType(), True)
])