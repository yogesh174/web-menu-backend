import os

def mkdir(name):
    a = os.system("mkdir {}".format(name))
    return a

def pwd():
    a = os.system("pwd")
    return a

def ifconfig():
    a = os.system("ifconfig")
    return a

def date():
    a = os.system("date")
    return a

def cal():
    a = os.system("cal")
    return a

def alias(name,work):
    a = os.system("alias {}='{}'".format(name,work))
    return a

def yum(name):
    a = os.system("yum install {} -y".format(name))
    return a

def whoami():
    a = os.system("whoami")
    return a

def lscpu():
    a = os.system("lscpu")
    return a

def inits():
    a = os.system("init 0")
    return a

def initr():
    a = os.system("init 6")
    return a

def free():
    a = os.system("free -m")
    return a

def ps():
    a = os.system("ps -aux")
    return a

def netstat():
    a = os.system("netstat -tnlp")
    return a

def ping(ip):
    a = os.system("ping {}".format(ip))
    return a

def disk_usage():
    a = os.system("df -h")
    return a