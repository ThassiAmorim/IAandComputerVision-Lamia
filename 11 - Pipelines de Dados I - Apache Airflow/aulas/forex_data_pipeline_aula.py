import airflow
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.email.operators.email import EmailOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from datetime import datetime, timedelta

import csv
import requests
import json

#
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 3, 26),
    "depends_on_past": False,  # nao depende de execuções passadas
    "email_on_failure": False,  # nao envia email em caso de falha
    "email_on_retry": False,  # nao envia email em caso de nova tentativa
    "email": "xxx.xxx@gmail.com",
    "retries": 1,  # num de tentativas em caso de falha
    "retry_delay": timedelta(minutes=5),  # intervalo entre tentativas
}


def download_rates():
    with open(
        "/usr/local/airflow/dags/files/forex_currencies.csv"
    ) as forex_currencies:  # abre o arquivo CSV
        reader = csv.DictReader(forex_currencies, delimiter=";")  # le como dicionario
        for row in reader:  # percorre as linhas do arquivo
            base = row["base"]
            with_pairs = row["with_pairs"].split(" ")
            indata = requests.get(
                "https://api.exchangeratesapi.io/latest?base=" + base
            ).json()  # requisicao da API
            outdata = {
                "base": base,
                "rates": {},
                "last_update": indata["date"],
            }  # dicionario de saida
            for pair in with_pairs:  # Itera sobre os pares de moedas
                outdata["rates"][pair] = indata["rates"][
                    pair
                ]  # guarda taxa de cambio no dicionario
            with open(
                "/usr/local/airflow/dags/files/forex_rates.json", "a"
            ) as outfile:  # abre o JSON para escrita
                json.dump(outdata, outfile)
                outfile.write("\n")


# cria a DAG
with DAG(
    dag_id="forex_data_pipeline_final",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
) as dag:

    # verifica se a API ta online
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates"
        in response.text,  # verifica se a resposta contem "rates"
        poke_interval=5,  # intervalo entre verificações
        timeout=20,  # tempo de espera maximo
    )

    # verifica se o CSV ta disponivel
    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20,
    )

    # operador Python para baixar taxas do cambio
    downloading_rates = PythonOperator(
        task_id="downloading_rates",  # nome da tarefa no airflow
        python_callable=download_rates,  # função Python a ser executada
    )

    # operador Bash para salvar taxas de ambio no HDFS
    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex && \
            hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
            """,  # comando bash para criar a pasta e salvar o arquivo
    )

    # operador Hive para criar uma tabela Hive externa
    creating_forex_rates_table = HiveOperator(
        task_id="creating_forex_rates_table",
        hive_cli_conn_id="hive_conn",
        hql="""
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING,
                last_update DATE,
                eur DOUBLE,
                usd DOUBLE,
                nzd DOUBLE,
                gbp DOUBLE,
                jpy DOUBLE,
                cad DOUBLE
            )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE
        """,
    )

    # operador Spark para processar os dados
    forex_processing = SparkSubmitOperator(
        task_id="forex_processing",
        conn_id="spark_conn",
        application="/usr/local/airflow/dags/scripts/forex_processing.py",  # path do script Spark
        verbose=False,
    )

    # operador para enviar email
    sending_email_notification = EmailOperator(
        task_id="sending_email",
        to="airflow_course@yopmail.com",
        subject="forex_data_pipeline",
        html_content="""
            <h3>forex_data_pipeline succeeded</h3>
        """,
    )

    # operador para enviar mensagem no Slack
    sending_slack_notification = SlackWebhookOperator(
        task_id="sending_slack",
        slack_webhook_conn_id="slack_conn",
        message="DAG forex_data_pipeline: DONE",  # texto da mensagem
    )

    # ordem de execucao das tarefas
    (
        is_forex_rates_available
        >> is_forex_currencies_file_available
        >> downloading_rates
        >> saving_rates
    )
    saving_rates >> creating_forex_rates_table >> forex_processing
    forex_processing >> sending_email_notification >> sending_slack_notification
