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


if option == "create a keypair":
    keypair_name = form["keypair_name"].strip()
    print("Creating KeyPair ...")
    response = create_keypair(keypair_name)
    # path = input("Enter the path to save Keypair: ").strip()
    # print("Saving KeyPair ...")
    # with open(os.path.join(path,'{}.pem'.format(response['KeyName'])), 'w') as file:
    #     file.write(response['KeyMaterial'])
    # print("Created and saved KeyPair")

elif option == "delete a keypair":
    keypair_name = form["keypair_name"].strip()
    print("Deleting KeyPair ...")
    response = delete_keypair(keypair_name)                        
    # print(response)
    print("Deleted KeyPair")

elif option == "list keypairs":
    response = list_keypairs()
    t = PrettyTable(['KeyPairId', 'KeyName'])
    for keypair in response['KeyPairs']:
        t.add_row([keypair['KeyPairId'], keypair['KeyName']])
    print(t)

else:
    print("Option not supported")