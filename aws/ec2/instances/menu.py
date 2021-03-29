#!/usr/bin/python3

import subprocess as sp
import json, sys

import cgi
import os

print("Content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()


from lvm_commands import *

form = json.load(sys.stdin)
option = form.get("option")


if option == "launch Instances":    
    subnet = input("Enter Subnet ID(default - default subnet): ")
    name = input("Enter Name(default- auto): ") or "auto"
    ami = input("Enter AMI ID(default- ami-098f16afa9edf40be): ") or "ami-098f16afa9edf40be"
    instance_type = input("Enter Instance Type(default- t2.micro): ") or "t2.micro"

    keypair = input("Enter key pair name(default - None): ")
    sg_id = input("Enter Security Group ID(default - 'default' SG): ")
    count = input("Enter count of instances(default- 1):") or '1'
    count = int(count)
    # ami and count required
    subnet = subnet.strip() 
    keypair = keypair.strip()
    sg_id = sg_id.strip()
    
    response = create_instance(ami, instance_type, count, subnet, sg_id, keypair, name)

elif option == "list Instances":
    list_instances()

elif option == "stop Instances":
    instance_id = input("Enter the instance id: ")
    
    response = stop_instance(instance_id)

    print("{} instance Stopped".format(instance_id))

elif option == "start Instances":
    instance_id = input("Enter the instance id: ")
    
    response = start_instance(instance_id)
    
    IP = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    print("Public IP: {}".format(IP))
    # txt = f"ssh ec2-user@{IP} -i C:\\Users\\91733\\Desktop\\KeyPairs\\keypair2.pem"
    # print(txt)
    # copy2clip(txt)

elif option == "terminate Instance":
    instance_id = input("Enter the instance id: ")
    terminate_instance(instance_id)

elif option == "get instance details":
    instance_id = input("Enter the instance id: ")
    describe_instance(instance_id)

elif option == "return to previous menu":
    break
else :
    print("Option not supported")