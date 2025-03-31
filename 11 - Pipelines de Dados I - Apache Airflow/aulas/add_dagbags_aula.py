import os  

from airflow.models import DagBag #para carregar DAGs dinamicamente
 

# caminhos absolutos das DAgs
dags_dirs = [  
    '/usr/local/airflow/project_a', 
    '/usr/local/airflow/project_b'  
]  

for dir in dags_dirs:  
    # cria uma instancia de DagBag para carregar todas as DAGs da pasta
    dag_bag = DagBag(os.path.expanduser(dir))  

    # se dag_bag foi criada com sucesso
    if dag_bag:  
        # itera sobre todas as DAGs carregadas no dag_bag
        for dag_id, dag in dag_bag.dags.items():  
            # adiciona a DAG ao escopo global pra que o airflow encontre
            globals()[dag_id] = dag  
