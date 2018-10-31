# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/10/31 下午6:33
"""
import os

from airflow.utils import email
from scr.email import template

base_path = os.path.dirname(__file__) + '/{}.html'


class Email:
    def __init__(self,
                 to, subject, html_content=None, files=None,
                 dryrun=False, cc=None, bcc=None,
                 mime_subtype='mixed'):
        # self.task_id = 'demo'
        self.to = to
        self.subject = subject
        self.html_content = html_content
        self.files = files
        self.dryrun = dryrun
        self.cc = cc
        self.bcc = bcc
        self.mime_subtype = mime_subtype

    def send_email(self):
        # email = EmailOperator(to=self.to, task_id=self.task_id, subject=self.subject, html_content=self.html_content)
        # email.execute(context=None)
        email.send_email(to=self.to, subject=self.subject, html_content=self.html_content)
        email.send_email(**vars(self))

    def send_email_template(self, file_name, kargs=None):
        if isinstance(kargs, dict):
            self.html_content = get_html_content(file_name, kargs)

        self.send_email()


def get_html_content(file_name, dicts):
    c = getattr(template, file_name)
    for i in dicts.keys():
        c = c.replace('[{}]'.format(i), str(dicts.get(i)))
    return c
