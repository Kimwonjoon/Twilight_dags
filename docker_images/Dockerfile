FROM apache/airflow:slim-2.9.3-python3.11

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

USER airflow

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY entrypoint.sh /opt/airflow/entrypoint.sh

ENTRYPOINT [ "/opt/airflow/entrypoint.sh" ]

USER airflow