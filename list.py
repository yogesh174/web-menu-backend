#!/usr/bin/python3

print("Content-type: application/json")
print("Access-Control-Allow-Origin: *")
print()

import subprocess as sp
import json, sys

import cgi
import os


form = json.load(sys.stdin)
# /aws/ec2
directory = form.get("directory")

# ./aws/ec2/list.py
path = "./" + directory + "/list.json"

with open(path) as f:
      data = json.load(f)
print(json.dumps(data))
