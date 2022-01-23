# Step -1
# Modules
from airflow import DAG
from datetime import datetime, timedelta
# Because we need to define tasks and in order to defined we will be using operator!
from airflow.operator.dummy_operator import DummyOperator

# Step -2
# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(22, 1, 23),
    'retries': 0
}

# Step -3
# Instantiate the DAG
dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')

# Step -4
# Define tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Step -5
# Define dependecies
start >> end