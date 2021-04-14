import subprocess
import boto3

ec2 = boto3.client('ec2')

def list_keypairs():
    response = ec2.describe_key_pairs()
    return response

def create_keypair(keypair_name):
    response = ec2.create_key_pair(KeyName=keypair_name)
    return response

def delete_keypair(keypair_name):
    response = ec2.delete_key_pair(KeyName=keypair_name)
    return response