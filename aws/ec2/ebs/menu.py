#!/usr/bin/python3

import subprocess as sp
import json, sys
import cgi
import os
from botocore.exceptions import ClientError
from prettytable import PrettyTable

print("Content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

from commands import *

form = json.load(sys.stdin)
option = form.get("option")


if option == "create volume":
    az = form['az'].strip()
    size = int(str(form['size']).strip())
    vt = form['vt'].strip()
    name = form['name'].strip()
    
    response = create_volume(az, size, vt='gp2', name='auto')
    print("Volume with volume id {} created".format(response['VolumeId']))

elif option == "create and attach volume":
    az = form['az'].strip()
    size = int(str(form['size']).strip())
    vt = form['vt'].strip()
    name = form['name'].strip()
    device_name = form["device_name"].strip()
    instance_id = form["instance_id"].strip()

    response = create_and_attach_volume(az, size, instance_id, device_name, vt='gp2', name='auto')
    print("Volume with volume id {} created".format(response['VolumeId']))

elif option == "attach volume":
    vol_id = form["vol_id"].strip()
    instance_id = form["instance_id"].strip()
    device_name = form["device_name"].strip()
    try :
        response = attach_volume(vol_id, instance_id, device_name)
        print(response)
    except ClientError as e:
        print("Check if they are in same region")
        print(e)

elif option == "detach volume":
    vol_id = form["vol_id"].strip()
    response = detach_volume(vol_id)
    print(response)

elif option == "list volumes":
    response = list_volumes()
    t = PrettyTable(['VolumeId', 'InstanceId', 'AvailabilityZone', 'Size', 'State'])
    
    for volume in response['Volumes']:
        try:
            t.add_row([volume['VolumeId'], volume['Attachments'][0].get('InstanceId', ''),  volume['AvailabilityZone'], volume['Size'], volume['State']])
        except IndexError:
            t.add_row([volume['VolumeId'], '-',  volume['AvailabilityZone'], volume['Size'], volume['State']])
    print(t)


elif option == "delete volume":
    vol_id = form["vol_id"].strip()
    try:
        res = delete_volume(vol_id)
        print(res)
    except ClientError as e:
        print("Make sure that volume is detached")
        print(e)

elif option == "get volume details":
    vol_id = form["vol_id"].strip()
    response = get_volume_details(vol_id)

    t = PrettyTable(['VolumeId', 'InstanceId', 'AvailabilityZone', 'Size', 'State'])
    
    volume = response['Volumes'][0]

    try:
        t.add_row([volume['VolumeId'], volume['Attachments'][0].get('InstanceId', ''),  volume['AvailabilityZone'], volume['Size'], volume['State']])
    except IndexError:
        t.add_row([volume['VolumeId'], '-',  volume['AvailabilityZone'], volume['Size'], volume['State']])
    print(t)

else :
    print("Option not supported")