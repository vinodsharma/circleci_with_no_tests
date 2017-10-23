from pyspark.sql import SparkSession
import os.path
import sys
# needed for relative import as src is in sibling folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from src import logging_utils
    logger = logging_utils.get_logger()
except:
    raise


def test_spark_json():
    LOGDNA_KEY = "2e65815d0b554429ade7a2449441597a"
    LOGDNA_APP = "test_spark_app"
    BUGSNAG_KEY = "8edf518b6fbd353085a6599f91cba0a8"
    BUGSNAG_RELEASE_STAGE = "staging"
    logger = logging_utils.get_app_logger(
        LOGDNA_KEY, LOGDNA_APP,
        BUGSNAG_KEY, BUGSNAG_RELEASE_STAGE
    )
    try:
        logger.info("test_spark_json started")
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        in_data_dir = os.path.join(cur_dir, "test_data/")
        sample_campaigns_file = os.path.join(
            in_data_dir, "sample-campaigns.json")
        spark = SparkSession.builder.master("local").appName(
            "Spark Tests").config(
                "spark.some.config.option", "some-value").getOrCreate()
        # dfjson = spark.read.json("/tmp/*.json")
        # dfjson = spark.read.json(
        #     "s3n://gobble-analytics/archive/mailchimp/campaigns/*.json")
        dfjson = spark.read.json(sample_campaigns_file)
        dfjson.printSchema()
        dfjson.createOrReplaceTempView("json_view")
        df = spark.sql("select explode(_links) from json_view")
        df.printSchema()
        # df = dfjson.select(explode("_links"))
        # df.printSchema()
        # raise ValueError("Custom Exception")

        # result = spark.sql(sqlstmt).take(1)
        # print(result)
        logger.info("test_spark_json ended")
        # raise ValueError("test_spark_json testing bugsnag with spark")
    except Exception:
        # logger.exception("test_spark_json Unhandled Exception")
        # raise ValueError("test_spark_json testing bugsnag with spark")
        raise



if __name__ == "__main__":
    test_spark_json()
