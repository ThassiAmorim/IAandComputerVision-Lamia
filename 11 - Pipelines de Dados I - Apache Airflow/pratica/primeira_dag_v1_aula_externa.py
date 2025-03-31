from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

minha_DAG = DAG(
    dag_id="a_primeira_DAG_v1",
    start_date=datetime(2025, 3, 26),
    schedule="@daily",
    doc_md=__doc__,
)
start = EmptyOperator(task_id="start", dag=minha_DAG)
hello = BashOperator(task_id="hello", bash_command="echo hello world", dag=minha_DAG)
end = EmptyOperator(task_id="end", dag=minha_DAG)

(start >> hello >> end)
