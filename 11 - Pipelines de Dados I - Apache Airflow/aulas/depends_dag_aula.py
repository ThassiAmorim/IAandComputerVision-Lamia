from airflow import DAG  


from airflow.operators.bash_operator import BashOperator  
from airflow.operators.python_operator import PythonOperator  
from datetime import datetime, timedelta  

default_args = {  
    'start_date': datetime(2019, 1, 1),  
    'owner': 'Airflow' 
}  

def second_task():  
    print('Hello from second_task')  
    raise ValueError('This will turns the python task in failed state') 

def third_task():  
    print('Hello from third_task') 
    raise ValueError('This will turns the python task in failed state') 

with DAG(  
    dag_id='depends_task', 
    schedule_interval="0 0 * * *",  # executa todo dia meia-noite
    default_args=default_args 
) as dag:  

    # task1 printa first task
    bash_task_1 = BashOperator(  
        task_id='bash_task_1',  # Identificador único da task dentro da DAG
        bash_command="echo 'first task'"  # comando bash 
    )  

    # task 2 printa second_task
    python_task_2 = PythonOperator(  
        task_id='python_task_2',  
        python_callable=second_task  #função python
    )  

    # task 2 printa third_task
    python_task_3 = PythonOperator(  
        task_id='python_task_3',  
        python_callable=third_task 
    )  

    # sequencia de execucao das tasks
    bash_task_1 >> python_task_2 >> python_task_3  
