"""imports"""
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.master("local[*]") \
        .appName("spark_processing") \
        .config("spark.driver.memory", "3G") \
        .config("spark.sql.shuffle.partitions", "8") \
        .config("spark.sql.execution.arrow.enabled", "true") \
        .config("spark.sql.execution.arrow.fallback.enabled", "true") \
        .config("spark.sql.repl.eagerEval.enabled", "true") \
        .getOrCreate()


def write_to_parquet(dataframe: DataFrame, path: str) -> None:
    """saves dataframe as a parquet file"""
    dataframe.write.mode('append').parquet(path)

def save_to_dataframe(data: list, schema: StructType) -> DataFrame:
    """converts list to dataframe"""
    dataframe = spark.createDataFrame(data, schema=schema)
    return dataframe