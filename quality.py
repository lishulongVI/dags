# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/10/31 下午7:06
"""

from __future__ import print_function

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from scr.quality.prod import ppt_email

args = {
    'owner': 'lishulong',
    'start_date': airflow.utils.dates.days_ago(2),
    'depends_on_past': False,
}

dag = DAG(
    dag_id='python_quality', default_args=args,
    schedule_interval='0 0 * * *'

)

s2 = PythonOperator(
    task_id='prod_email',
    provide_context=True,
    python_callable=ppt_email(),
    dag=dag)
