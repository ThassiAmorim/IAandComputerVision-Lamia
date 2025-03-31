from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta


default_args = {
    "start_date": datetime(2025, 3, 29, 1), #inicio da DAG - 29 de marco de 2025 - 1 da manha
    "owner": "Airflow"}

with DAG(
    dag_id="start_and_schedule_dag",
    schedule_interval="0 * * * *",
    default_args=default_args,
) as dag:

    dummy_task_1 = DummyOperator(task_id="dummy_task_1")  # task1

    dummy_task_2 = DummyOperator(task_id="dummy_task_2")  # task2

    dummy_task_1 >> dummy_task_2  # dummy_task_1 executa antes de dummy_task_2
