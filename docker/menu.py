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


if option == "launch a docker container" :
    image = form["image"].strip()
    name = form["name"].strip()

    cid = launch_docker_container(image=image, name=name)
    print(cid)

elif option == 'list docker containers' :
    containers = list_containers()
    print(containers)

elif option == "remove one container":
    name = form["name"].strip()
    remove_containers(name=name)

elif option == "remove one container focefully":
    name = form["name"].strip()
    remove_containers(name=name , force=True)

elif option == "remove all stopped containers":
    remove_containers(all_stopped=True)

elif option == "remove all containers":
    remove_containers(all_running=True)

elif option == "stop a container":
    name = form["name"].strip()
    stop_container(name=name)

elif option == "start a container":
    name = form["name"].strip()
    start_container(name=name)

elif option == "copy file to container":
    name = form["name"].strip()
    src = form["src"].strip()
    dest = form["dest"].strip()
    copy_to_container(name, src, dest)

elif option == "copy file from container":
    name = form["name"].strip()
    src = form["src"].strip()
    dest = form["dest"].strip()
    copy_from_container(name, src, dest)

elif option == "run a command on specific container":
    name = form["name"].strip()
    cmd = form["cmd"].strip()
    op = exec_command(name=name, cmd=cmd)
    print(op)

elif option == "pull an image":
    name = form["name"].strip()
    pull_image(name=name)

elif option == "list images":
    images = list_images()
    print(images)

elif option == "remove image":
    name = form["name"].strip()
    remove_image(name=name)

elif option == "search for images on dockerhub":
    name = form["name"].strip()
    op = search_image(name=name)
    print(op)
    
elif option == "check logs on a container":
    name = form["name"].strip()
    logs = container_logs(name)
    print(logs)

elif option == "know docker version":
    version = docker_version()
    print(version)

elif option == "know docker info":
    info = docker_info()
    print(info)

elif option == "custom linux command":
    cmd = form["cmd"].strip()
    op = subprocess.getoutput(cmd)
    print(op)

elif option == "start docker daemon":
    start_docker()

elif option == "stop docker daemon":
    stop_docker()

elif option == "know status of docker daemon":
    status = get_status_docker()
    print(status)

else :
    print("Option not supported")