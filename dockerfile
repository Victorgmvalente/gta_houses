FROM python:3.8-slim-buster

# Utils
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install wget curl vim net-tools g++

# Install Java
RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz -P /usr/local/.
RUN tar -xzvf /usr/local/jdk-8u131-linux-x64.tar.gz -C /usr/local/
RUN ln -s /usr/local/jdk1.8.0_131/ /usr/local/java
ENV JAVA_HOME "/usr/local/java"
ENV PATH "$JAVA_HOME/bin:$PATH"

# Python and Dependencies
RUN pip install --upgrade pip
RUN pip install --no-input -U notebook pandas numpy scikit-learn statsmodels joblib tensorflow matplotlib imbalanced-learn wordcloud pyspark scrapy shap mlflow xgboost ipywidgets widgetsnbextension pandas-profiling kedro kedro-viz

ENV PYSPARK_SUBMIT_ARGS "--packages io.delta:delta-core_2.12:0.8.0,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog pyspark-shell"
