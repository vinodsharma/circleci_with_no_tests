FROM gobble/python:3.6

ENV SPARK_HOME=/usr/local/bin/spark
ENV PYSPARK_PYTHON=/usr/local/bin/python3.6
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/python3.6
ENV PYTHONHASHSEED=0

RUN yum update -y
RUN yum -y install java-1.8.0
RUN virtualenv -p python3 $VENV_DIR \
  && source $VENV_DIR/bin/activate \
  && python --version \
  && pip --version \
  && wget https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz \
  && tar xvzf spark-*.tgz > /tmp/spark-ec2_spark.log \
  && rm spark-*.tgz \
  && mv `ls -d spark-* | grep -v ec2` $SPARK_HOME \
  && pip install --upgrade --no-cache-dir pyspark \
  && wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.8.1/hadoop-aws-2.8.1.jar \
  && mv hadoop-aws-2.8.1.jar $SPARK_HOME/jars/ \
  && wget https://sdk-for-java.amazonwebservices.com/latest/aws-java-sdk.zip \
  && unzip aws-java-sdk.zip \
  && cp aws-java-sdk-*/lib/aws-java-sdk-*.jar $SPARK_HOME/jars/ \
  && rm -rf  aws-java-sdk-*
