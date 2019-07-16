# -*- coding:utf-8 -*-
# __author__ = "MuT6 Sch01aR"
import paramiko
import pathlib
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


# 定义工作
def job_function():
    filename = datetime.now().strftime('%Y%m%d-%H%M%S') + ".txt"
    pathlib.Path(filename).touch()
    print("成功创建文件：" + filename)

    transport = paramiko.Transport(('172.16.74.39', 22))
    transport.connect(username='xia0sheng', password='wangyouyu')

    sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

    sftp.put(filename, '/'+filename)  # 将本地的filename.txt文件上传至服务器/filename.txt

    transport.close()  # 关闭连接


# 每5s执行一次
scheduler.add_job(job_function, 'interval', seconds=5)


scheduler.start()
