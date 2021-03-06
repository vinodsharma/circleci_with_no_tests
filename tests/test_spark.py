from pyspark.sql import SparkSession
import os.path


def test_spark_json():
    try:
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
        # raise ValueError("test_spark_json testing bugsnag with spark")
    except Exception:
        # logger.exception("test_spark_json Unhandled Exception")
        # raise ValueError("test_spark_json testing bugsnag with spark")
        raise


if __name__ == "__main__":
    test_spark_json()
