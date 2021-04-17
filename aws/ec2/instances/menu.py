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


if option == "launch Instances":    
    subnet = form["subnet"]
    name = form["name"]
    ami = form["ami"]
    instance_type = form["instance_type"]
    keypair = form["keypair"]
    sg_id = form["sg_id"]
    count = form["count"]

    count = int(count)
    # ami and count required
    subnet = subnet.strip() 
    keypair = keypair.strip()
    sg_id = sg_id.strip()
    
    response = create_instance(ami, instance_type, count, subnet, sg_id, keypair, name)
    if response:
        print("Instance Launched!")
        print(response)
    else:
        print("Unable to launch an instance!")
        print("Please check the details entered!!")

elif option == "list Instances":
    list_instances()

elif option == "stop Instances":
    instance_id = form["instance_id"]
    
    response = stop_instance(instance_id)

    print("{} instance Stopped".format(instance_id))

elif option == "start Instances":
    instance_id = form["instance_id"]
    
    response = start_instance(instance_id)
    
    IP = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    print("Public IP: {}".format(IP))

elif option == "terminate Instance":
    instance_id = form["instance_id"]
    terminate_instance(instance_id)

elif option == "get instance details":
    instance_id = form["instance_id"]
    describe_instance(instance_id)

else :
    print("Option not supported")
