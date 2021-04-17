#!/usr/bin/python3
import subprocess
import os
import shlex

def get_ip(interface=""):
    if not interface:
        interface = subprocess.getoutput("route | awk '/default/ {print $8}'")
    ip = subprocess.getoutput("ifconfig {0}".format(interface) + " | awk '/inet / {print $2}'")
    return ip

def docker_version():
    version = subprocess.getoutput("docker version")
    return version

def docker_info():
    info = subprocess.getoutput("docker info")
    return info

def stop_docker():
    subprocess.getoutput("sudo systemctl stop docker")
    print("Stopped docker daemon!")

def start_docker():
    subprocess.getoutput("setenforce 0")
    subprocess.getoutput("sudo systemctl start docker")
    print("Started docker daemon!")

def get_status_docker():
    status = subprocess.getoutput("systemctl status docker")    
    return status

def list_containers():
    containers = subprocess.getoutput("docker ps -a")
    return containers

def list_images() :
    images = subprocess.getoutput("docker images")
    return images

def pull_image(name):
    subprocess.getoutput("docker image pull {}".format(name))
    print("Downloaded docker image {}".format(name))

def remove_image(name) :
    subprocess.getoutput("docker image rm {}".format(name))
    print("Removed docker image {}".format(name))

def launch_docker_container(image, name, detach=""):
    cmd = "docker run -dit "
    if name.strip() :
        cmd = cmd + " --name {} ".format(name)

    cmd = cmd + " {} ".format(image)
    cid = subprocess.getoutput(cmd)
    print("Launched Container!")
    return cid

def remove_containers(name='', force=False, all_running=False, all_stopped=False):
    if name and (not force):
        print("Removing container {} ...".format(name))
        subprocess.getoutput('docker container rm {}'.format(name))
    elif force:
        print("Removing container {} forcefully ...".format(name))
        subprocess.getoutput('docker container rm -f {}'.format(name))
    elif all_running:
        print("Removing all running containers ...")
        subprocess.getoutput('docker container rm -f $(docker ps -aq)')
    elif all_stopped:
        print("Removing all stopped containers ...")
        subprocess.getoutput('docker container rm $(docker ps -aq)')

def stop_container(name):
    subprocess.getoutput("docker container stop {}".format(name))
    print("Stopped container {} ...".format(name))

def start_container(name):
    subprocess.getoutput("docker container start {}".format(name))
    print("Started container {} ...".format(name))

def exec_command(name, cmd):
    op = subprocess.getoutput("docker container exec {} {}".format(name, cmd))
    return op

def search_image(name):
    print("Searching for {} ...".format(name))
    op = subprocess.getoutput("docker search {}".format(name))
    return op

def container_logs(name):
    print("Obtaining logs for {} ...".format(name))
    logs = subprocess.getoutput("docker logs {}".format(name))
    return logs

def copy_to_container(name, src, dest):
    subprocess.getoutput("docker cp {} {}:{}".format(src, name, dest))
    print("Copied {} to Container {} at {} ...".format(src, name, dest))
    
def copy_from_container(name, src, dest):
    subprocess.getoutput("docker cp {}:{} {}".format(name, src, dest))
    print("Copied {} from Container {} at {} ...".format(src, name, dest))
    