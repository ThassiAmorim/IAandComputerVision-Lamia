from airflow import DAG  
from airflow.operators.bash_operator import BashOperator  
from datetime import datetime, timedelta  

default_args = {  
    'start_date': datetime(2025, 1, 1),  
    'owner': 'Airflow' 
}  

with DAG(  
    dag_id='backfill', 
    schedule_interval="0 0 * * *",  # agendamento da DAG
    default_args=default_args, 
    catchup=False  #execucoes atrasadas nao sao realizadas automaticamente
) as dag:  

    # task 1 printa first task
    bash_task_1 = BashOperator(  
        task_id='bash_task_1',  
        bash_command="echo 'first task'"  
    )  

    # task 2 printa second task
    bash_task_2 = BashOperator(  
        task_id='bash_task_2',  
        bash_command="echo 'second task'" 
    )  

    # bash_task_1 ocorre antes de bash_task_2
    bash_task_1 >> bash_task_2  
