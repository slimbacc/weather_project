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


def read_from_parquet(parquet_file_path: str) -> DataFrame:
    """read dfs from parquet files"""
    return spark.read.parquet(parquet_file_path)


def create_df_with_schema(
        dataframe: DataFrame,
        schema: StructType) -> DataFrame:
    """Create a dataframe and enforce the given schema."""
    return spark.createDataFrame(
        schema=schema, data=spark.sparkContext.emptyRDD()
    ).union(dataframe)
