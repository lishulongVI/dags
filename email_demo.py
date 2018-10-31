# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/10/31 下午4:32
"""

# https://airflow.incubator.apache.org/code.html
import datetime
from airflow.operators.email_operator import EmailOperator
from airflow.models import DAG

default_args = {
    'owner': 'lishulong',
    'start_date': datetime.datetime(year=2018, month=9, day=17),
    'depends_on_past': False
}

dag = DAG(
    dag_id='email_demo',
    default_args=default_args,
    schedule_interval='0 1/* * * *'
)

email = EmailOperator(
    dag=dag,
    task_id='email',
    retries=False,
    to='lishulong.never@gmail.com',
    subject='this is a test subject',
    html_content='<html>this is html content</html>',
    cc='lishulong.never@gmail.com',
    bcc='lishulong.never@gmail.com',
    mime_subtype='mixed')
