# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/10/31 下午3:47
"""
from scr.email.email_util import Email


def ppt():
    from datetime import datetime
    print('*' * 20)
    date = 'product time:', datetime.now()

    print(date)


def ppt_email():
    from datetime import datetime
    print('*' * 20)
    date = 'product time: {}'.format(datetime.now())
    quality = {'count': 1, 'summary_1': 200}
    if True:
        Email(to='lishulong.never@gmail.com', subject=date).send_email_template('quality', quality)


# print(ppt_email())
