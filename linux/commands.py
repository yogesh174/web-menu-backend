import os
import subprocess

def mkdir(name):
    a = subprocess.getoutput("sudo mkdir {}".format(name))
    return a

def pwd():
    a = subprocess.getoutput("sudo pwd")
    return a

def ifconfig():
    a = subprocess.getoutput("sudo ifconfig")
    return a

def date():
    a = subprocess.getoutput("sudo date")
    return a

def cal():
    a = subprocess.getoutput("sudo cal")
    return a

def alias(name,work):
    a = subprocess.getoutput("sudo alias {}='{}'".format(name,work))
    return a

def yum(name):
    a = subprocess.getoutput("sudo yum install {} -y".format(name))
    return a

def whoami():
    a = subprocess.getoutput("sudo whoami")
    return a

def lscpu():
    a = subprocess.getoutput("sudo lscpu")
    return a

def inits():
    a = subprocess.getoutput("sudo init 0")
    return a

def initr():
    a = subprocess.getoutput("sudo init 6")
    return a

def free():
    a = subprocess.getoutput("sudo free -m")
    return a

def ps():
    a = subprocess.getoutput("sudo ps -aux")
    return a

def netstat():
    a = subprocess.getoutput("sudo netstat -tnlp")
    return a

def disk_usage():
    a = subprocess.getoutput("sudo df -h")
    return a