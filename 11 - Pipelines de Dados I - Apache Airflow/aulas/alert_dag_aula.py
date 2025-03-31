from airflow import DAG  
from airflow.operators.bash_operator import BashOperator # pra executar comandos Bash dentro da DAG
from datetime import datetime, timedelta  

default_args = {  
    'start_date': datetime(2025, 1, 1),  # data de inicio da DAG
    'owner': 'Airflow' 
}  

with DAG(  
    dag_id='alert_dag',  # nome da DAG dentro do airflow
    schedule_interval="0 0 * * *",  # agendamento da DAG (executa todo dia meia noite)
    default_args=default_args,  
    catchup=True  # permite execuções atrasadas
) as dag:  

    # task 1 executa um comando bash que retorna exit 1
    t1 = BashOperator(  
        task_id='t1', 
        bash_command="exit 1" 
    )  

    # task 2 executa um comando bash que printa second task
    t2 = BashOperator(  
        task_id='t2', 
        bash_command="echo 'second task'" 
    )  

    # t1 deve ser concluída antes de t2 ser executada
    t1 >> t2  
