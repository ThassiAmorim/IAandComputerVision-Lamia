import pendulum
from airflow import DAG 
from airflow.operators.empty import EmptyOperator 
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta 

# usa o fuso horario de sao paulo
local_tz = pendulum.timezone("America/Sao_Paulo")

default_args = {
    'start_date': datetime(2025, 3, 29),  # inicia dia 29 de marco de 2025
    'owner': 'airflow', 
    'retries': 2,  # tenta 2 vezes em caso de falha
    'retry_delay': timedelta(minutes=5)  # espera 5 min entre as tentativas
}

# funcao python que simula o processamento dos pedidos
def process_orders():
    print("Processando pedidos...")

# simula o processamento de uma certa categoria de pedidos
def categorize_order(category):
    print(f"Processando pedidos da categoria: {category}")

with DAG(
    dag_id='Loja_da_Thassi',  # nome da DAG no Airflow
    schedule="0 2 * * *",  # executa todo dia as 2 da manha 
    default_args=default_args, 
    catchup=False  # impede execucoes anteriores
) as dag:

    # primeira task marca o inicio da DAG
    start = EmptyOperator(task_id='start')  

    # task 2 simula baixar os pedidos do banco com o BashOperator
    fetch_orders = BashOperator(
        task_id='fetch_orders',
        bash_command="echo 'Baixando pedidos do banco de dados...'" 
    )

    # chama uma funcao pra processar os pedidos
    process_orders_task = PythonOperator(
        task_id='process_orders',
        python_callable=process_orders 
    )

    # categorias de pedidos
    categories = ['eletronicos', 'roupas', 'alimentos']

    # cria dinamicamente uma task para cada categoria de pedidos
    categorize_tasks = [
        PythonOperator(
            task_id=f'categorize_{category}',  # gera um ID para cada categoria
            python_callable=categorize_order,  # chama a funcao que processa a categoria
            op_args=[category]  # passa o nome da categoria como argumento para a função
        ) for category in categories
    ]

    # task 3 para o relatorio final dos pedidos
    generate_report = BashOperator(
        task_id='generate_report',
        bash_command="echo 'Gerando relatório final...'"
    )

    # ultima task com EmptyOperator
    end = EmptyOperator(task_id='end') 

    # fluxo
    start >> fetch_orders >> process_orders_task >> categorize_tasks >> generate_report >> end
   
    # Fluxo:
    # 1. inicia com 'start'
    # 2. baixa os pedidos 'fetch_orders'
    # 3. processa os 'process_orders_task'
    # 4. processa categorias dinamicamente 'categorize_tasks'
    # 5. cria relatorio 'generate_report'
    # 6. ultima task 'end'