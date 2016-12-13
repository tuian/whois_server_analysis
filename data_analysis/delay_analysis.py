# encoding:utf-8
"""
To analyze the delay variation of sever
"""

from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np


def get_db():
    """
    获取数据库
    :return
    """
    client = MongoClient('localhost', 27017)
    db = client['whois_sever_analysis']
    return db


def get_delay():

    delays = []
    db = get_db()
    col = db['ip_net_state']
    ip_delay = col.find({},{'_id':0,'delay':1})
    for i in ip_delay:
        delays.append(i['delay'])

    return delays

def draw():
    domain = 'taobao.com'

    fig = plt.figure(1, figsize=(8.5, 5), dpi=75)
    delays = get_delay()
    # delays.sort()
    in_x = np.arange(len(delays))
    fig.add_subplot(111)

    plt.plot(in_x,delays, 'o')
    plt.ylabel('Delay Time(s)')
    plt.xlabel('Server Sequence')

    plt.savefig('./graph/delay_time.png', dpi=75)
    plt.show()


draw()














