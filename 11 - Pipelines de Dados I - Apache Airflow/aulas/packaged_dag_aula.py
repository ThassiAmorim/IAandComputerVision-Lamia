import os  
from airflow.models import DagBag  

#pastas com o caminho absoluto das dags
dags_dirs = [  
    '/usr/local/airflow/project_a', 
    '/usr/local/airflow/project_b'  
]  

for dir in dags_dirs:  
    # carrega  todas as DAGs 
    dag_bag = DagBag(os.path.expanduser(dir))  

    if dag_bag:  
        for dag_id, dag in dag_bag.dags.items():  
            # permite que o airflow encontre as DAGs
            globals()[dag_id] = dag  
