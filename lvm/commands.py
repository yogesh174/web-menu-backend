import subprocess
import os 

def create_pv(device_name):
    op = subprocess.getoutput("sudo pvcreate {}".format(device_name))
    return op

def list_all_pvs():
    op = subprocess.getoutput("sudo pvdisplay")
    return op

def list_pv(pv_name):
    op = subprocess.getoutput("sudo pvdisplay {}".format(pv_name))
    return op

def remove_pv(pv_name):
    op = subprocess.getoutput("sudo pvremove {}".format(pv_name))
    return op

def remove_vg(vg_name):
    op = subprocess.getoutput("sudo vgremove {}".format(vg_name))
    return op

def remove_lv(lv_path):
    unmount_lv(lv_path)
    op = os.system("lvremove {}".format(lv_path))
    return op


# TODO: Create a VG with multiple pv_names 
def create_vg(vg_name, pv_name):
    op = subprocess.getoutput("sudo vgcreate {} {}".format(vg_name, pv_name))
    return op

def list_all_vgs():
    op = subprocess.getoutput("sudo vgdisplay")
    return op

def list_vg(vg_name):
    op = subprocess.getoutput("sudo vgdisplay {}".format(vg_name))
    return op

def extend_vg(vg_name, pv_name):
    op = subprocess.getoutput("sudo vgextend {} {}".format(vg_name, pv_name))
    return op

def create_lv(size, lv_name, vg_name):
    op = os.system("lvcreate --size {} --name {} {}".format(size, lv_name, vg_name))
    return op

def list_all_lvs():
    op = subprocess.getoutput("sudo lvdisplay")
    return op

def list_lv(vg_name, lv_name):
    op = subprocess.getoutput("sudo lvdisplay {}/{}".format(vg_name, lv_name))
    return op

# TODO: 
# 1. Auto extract the path name from a given lv name
# 2. Give a choice for type of formatting instead of default ext4
def format_lv(lv_path):
    op = subprocess.getoutput("sudo mkfs.ext4 {}".format(lv_path))
    return op

def mount_lv(lv_path, mount_path):
    op = subprocess.getoutput("sudo mount {} {}".format(lv_path, mount_path))
    return op

def unmount_lv(lv_path):
    op = subprocess.getoutput("sudo umount {}".format(lv_path))
    return op

# TODO: Give a choice for dynamic units instead of only GBs 
def extend_lv(size, lv_path):
    op = subprocess.getoutput("sudo lvextend --size +{} {}".format(size, lv_path))
    subprocess.getoutput("sudo e2fsck -f {}".format(lv_path))
    subprocess.getoutput("sudo resize2fs {}".format(lv_path))
    return op

def reduce_lv_and_format(new_size, lv_path, mount_path):
    os.system("umount {}".format(lv_path))
    os.system("e2fsck -f {}".format(lv_path))
    os.system("resize2fs {} {}".format(lv_path, new_size))
    os.system("lvreduce --size {} {}".format(new_size, lv_path))
    os.system("mount {} {}".format(lv_path, mount_path))
    return "Reduced LV to {}".format(new_size)

# Displays disk information for all the file systems
def disk_space():
    op = subprocess.getoutput("sudo df -h")
    return op

def ask_choice():
    while True:
        try:
            option = int(input("Enter your option: "))
            break
        except ValueError:
            print("Enter a valid number")
    return option

def change_color(x):
    cmd = f"tput setaf {x}"
    os.system(cmd)

def mkdir(name):
    a = os.system("mkdir {}".format(name))
    return a