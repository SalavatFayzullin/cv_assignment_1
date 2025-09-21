from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import subprocess
import os

default_args = {
    'owner': 'mlops',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2025, 9, 21)
}

dag = DAG(
    'titanic_mlops_pipeline',
    default_args=default_args,
    description='Automated MLOps pipeline',
    schedule_interval='*/5 * * * *',
    catchup=False
)

def data_engineering():
    os.chdir('/opt/airflow/workspace')
    subprocess.run(['python', 'code/datasets/data_preprocessing.py'], check=True)

def model_engineering():
    os.chdir('/opt/airflow/workspace')
    subprocess.run(['python', 'code/models/train_model.py'], check=True)

def deployment():
    os.chdir('/opt/airflow/workspace/code/deployment')
    subprocess.run(['docker-compose', 'up', '--build', '-d'], check=True)

# Tasks
data_task = PythonOperator(
    task_id='data_engineering',
    python_callable=data_engineering,
    dag=dag
)

model_task = PythonOperator(
    task_id='model_engineering',
    python_callable=model_engineering,
    dag=dag
)

deploy_task = PythonOperator(
    task_id='deployment',
    python_callable=deployment,
    dag=dag
)

# Dependencies
data_task >> model_task >> deploy_task