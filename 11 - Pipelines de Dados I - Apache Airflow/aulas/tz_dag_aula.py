import pendulum  
from airflow import DAG  
from airflow.utils import timezone  
from airflow.operators.dummy_operator import DummyOperator  
from datetime import timedelta, datetime  
local_tz = pendulum.timezone("Europe/Paris")  

default_args = {  
    'start_date': datetime(2015, 3, 29, 1),  # inicio da DAG 29 de marco de 2025 1 da manha
    'owner': 'Airflow'
}  

with DAG(  
    dag_id='tz_dag',  # Nome da DAG no airflow
    schedule_interval="0 1 * * *",  # roda todo dia a 1 da manha
    default_args=default_args  
) as dag:  

    dummy_task = DummyOperator(task_id='dummy_task')  

    #pega as datas de execução da DAG
    run_dates = dag.get_run_dates(start_date=dag.start_date)  

    # encontra ultima data de execucao
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None  

    # printa infos da DAG

    print('datetime from Python is Naive: {0}'.format(timezone.is_naive(datetime(2019, 9, 19))))  

    print('datetime from Airflow is Aware: {0}'.format(timezone.is_naive(timezone.datetime(2019, 9, 19)) == False))  

    print('[DAG:tz_dag] timezone: {0} - start_date: {1} - schedule_interval: {2} - Last execution_date: {3} - next execution_date {4} in UTC - next execution_date {5} in local time'.format(
        dag.timezone, 
        dag.default_args['start_date'],  
        dag._schedule_interval,  # intervalo de execucao da DAG
        dag.latest_execution_date,  # ultima data de execucao da DAG
        next_execution_date,  # prox data de execucao
        local_tz.convert(next_execution_date) if next_execution_date is not None else None  
        # data convertida para o fuso horario local
    ))  
    
