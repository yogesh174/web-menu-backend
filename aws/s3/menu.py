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


if option == "create a bucket":
    bucket_name = form["bucket_name"].strip()
    region = form["region"].strip()
    response = create_bucket(bucket_name, region)
    if not response[0]:
        print("Bucket not created!!")
        print(response[1])
    else :
        print("Bucket created!")

elif option == "delete bucket":
    bucket_name = form["bucket_name"].strip()
    print("Deleting bucket {}".format(bucket_name))
    delete_bucket(bucket_name)
    print("Deleted bucket")


elif option == "list buckets":
    response = list_buckets()
                
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

elif option == "upload files to bucket":
    path = form["path"].strip()
    bucket_name = form["bucket_name"].strip()
    obj_name = form["obj_name"].strip()
    public = form["public"]
    if public.lower() == "y":
        public = True
    elif public.lower() == "n":
        public = False
    response = upload_file(path, bucket_name, obj_name, public)
    
    if not response[0]:
        print("File not uploaded")
        print(response[1])
    else :
        print("File uploaded")

    
elif option == "download files from bucket":
    bucket_name = form["bucket_name"].strip()
    obj_name = form["obj_name"].strip()
    path = form["path"].strip()
    download_file(bucket_name, obj_name, path)
    
elif option == "list files in bucket":
    bucket_name = form["bucket_name"].strip()
    response = list_files(bucket_name)
    # print(response)
    if response.get('Contents'):
        for key in response['Contents']:
            print(key['Key'])
    else:
        print("Bucket is empty!")

elif option == "delete file in bucket":
    bucket_name = form["bucket_name"].strip()
    obj_name = form["obj_name"].strip()
    response = delete_file(bucket_name, obj_name)
    print("Object deleted")

else :
    print("Option not supported")