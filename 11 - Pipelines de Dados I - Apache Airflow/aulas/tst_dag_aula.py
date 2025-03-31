from airflow import DAG  
from airflow.operators.dummy_operator import DummyOperator  
from airflow.operators.python_operator import PythonOperator  
from datetime import datetime, timedelta  

default_args = {  
    'start_date': datetime(2025, 1, 1)
}  

def process():  
    return 'process'

with DAG(  
    dag_id='tst_dag',  # nome da DAG no airflow
    schedule_interval='0 0 * * *',  # executa todo dia meia-noite
    default_args=default_args, 
    catchup=False  # nao roda execucoes passadas
) as dag:  

    # task 1 um DummyOperator que nao faz nada eh usado inicio da DAG
    task_1 = DummyOperator(task_id='task_1')  

    # task 2 executa a funcao python process
    task_2 = PythonOperator(  
        task_id='task_2',
        python_callable=process  
    )  

    # criação dinamica das tasks
    tasks = [DummyOperator(task_id='task_{0}'.format(t)) for t in range(3, 6)]  

    # task 6 ultima task
    task_6 = DummyOperator(task_id='task_6')  

    # task_1 -> task_2 -> (task_3, task_4, task_5) -> task_6
    task_1 >> task_2 >> tasks >> task_6  
