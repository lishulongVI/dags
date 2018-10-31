from __future__ import print_function

from airflow import utils
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from scr.quality.prod import ppt
from scr.quality.test import pt

args = {
    'owner': 'lishulong',
    'start_date': utils.dates.days_ago(2),
    'depends_on_past': False,
}

dag = DAG(
    dag_id='quality', default_args=args,
    schedule_interval='0 0 * * *'

)

s1 = PythonOperator(
    task_id='test',
    provide_context=True,
    python_callable=pt(),
    dag=dag)

s2 = PythonOperator(
    task_id='prod',
    provide_context=True,
    python_callable=ppt(),
    dag=dag)

s1.set_upstream(s2)