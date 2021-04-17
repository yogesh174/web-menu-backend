#!/usr/bin/python3

import subprocess as sp
import json, sys
import cgi
import os

print("Content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

from commands import *

form = json.load(sys.stdin)
option = form.get("option")

if option == "create a directory" :
    name = form["name"].strip()
    print(mkdir(name))

elif option == "display working directory" :
    pwd = pwd()
    print(pwd)

elif option == "display ip address" :
    ifconfig = ifconfig()
    print(ifconfig)

elif option == "display date" :
    date = date()
    print(date)
    
elif option == "display calender" :
    cal = cal()
    print(cal)

elif option == "create alias" :
    name = form["name"].strip()
    cmd = form["cmd"].strip()
    print(alias(name,cmd))

elif option == "install pkg" :
    name = form["name"].strip()
    print(yum(name))

elif option == "display the info of current user" :
    whoami = whoami()
    print(whoami)

elif option == "display cpu details" :
    lscpu = lscpu()
    print(lscpu)

elif option == "shutdown" :
    inits()
    
elif option == "reboot" :
    initr()

elif option == "display current memory usage" :
    free = free()
    print(free)

elif option == "display running process" :
    ps = ps()
    print(ps)
    
elif option == "display open ports" :
    netstat = netstat()
    print(netstat)

elif option == "display disk usage" :
    disk_usage = disk_usage()
    print(disk_usage)

else :
    print("Option not supported")