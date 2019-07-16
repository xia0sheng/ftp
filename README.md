# ftp
使用教程

1、接收服务器(远程) ftp环境搭建

    http://www.freesshd.com/?ctt=download 
    下载freeSSHd.exe文件
    
    配置教程参见：
    https://blog.csdn.net/imjcoder/article/details/79171660
    
2、本机 安装python环境


    https://www.python.org/downloads/release/python-374/
    
3、本机安装git


    https://git-scm.com/download/win
    
4、下载代码


    git clone https://github.com/xia0sheng/ftp.git
    cd ftp
    
    
5、配置环境
    virtualenv venv
    pip install -r requirements.txt
    
    Linux/Mac os激活环境：source venv/bin/activate 
    Windows下激活环境：venv/Scripts/activate
    修改text.py文件中的下面两行
    transport = paramiko.Transport(('172.16.74.39', 22))
    transport.connect(username='xia0sheng', password='wangyouyu')
    
    执行 python text.py 启动程序，没5s钟自动生成一个空文件上传到ftp服务器
    