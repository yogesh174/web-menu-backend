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


if option == "create a PV" :
    device_name = form["device_name"]
    op = create_pv(device_name)
    print(op)
    
elif option == "list PVs" :
    op = list_all_pvs()
    print(op)

elif option == "get details of a PV" :
    pv_name = form["pv_name"]
    op = list_pv(pv_name)
    print(op)
    
elif option == "remove a PV" :
    pv_name = form["pv_name"]
    op = remove_pv(pv_name)
    print(op)

elif option == "remove a VG" :
    vg_name = form["vg_name"]
    op = remove_vg(vg_name)
    print(op)

elif option == "remove an LV" :
    path = form["path"]
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = remove_lv(path, lv_path)
    print(op)

elif option == "create a VG" :    
    pv_name = form["pv_name"]
    vg_name = form["vg_name"]
    op = create_vg(vg_name, pv_name)
    print(op)

elif option == "list all the VGs" :
    op = list_all_vgs()
    print(op)
    
elif option == "get details of a VG" :
    vg_name = form["vg_name"]
    op = list_vg(vg_name)
    print(op)

elif option == "extend a VG" :
    pv_name = form["pv_name"]
    vg_name = form["vg_name"]
    op = extend_vg(vg_name, pv_name)
    print(op)

elif option == "create a LV" :
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    size = form["size"]
    op = create_lv(size, lv_name, vg_name)
    print(op)

elif option == "list all the LVs" :
    op = list_all_lvs()
    print(op)

elif option == "get details of an LV" :
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    op = list_lv(vg_name, lv_name)
    print(op)

elif option == "format an LV" :
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = format_lv(lv_path)
    print(op)

elif option == "mount an LV" :
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    mount_path = form["mount_path"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = mount_lv(lv_path, mount_path)
    print(op)
    print("Mounted Successfully")

elif option == "extend an LV" :   
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    size = form["size"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = extend_lv(size, lv_path)
    print(op)

elif option == "reduce an LV" :
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    size = form["size"]
    mount_path = form["mount_path"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = reduce_lv_and_format(size, lv_path, mount_path)
    print(op)

elif option == "unmount an LV":
    lv_name = form["lv_name"]
    vg_name = form["vg_name"]
    lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
    op = unmount_lv(lv_path)
    print(op)
    print("Unmounted Successfully")

elif option == "display the disk space" :
    op = disk_space()
    print(op)

elif option == "create a directory":
    dir_path = form["dir_path"]
    op = mkdir(dir_path)
    print("Created directory!")
else :
    print("Option not supported")