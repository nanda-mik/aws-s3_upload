import boto3
from botocore.client import Config
import os

env1 = os.environ.get('ACCESS_KEY_ID')
env2 = os.environ.get('ACCESS_SECRET_KEY')
env3 = 'node-s3-my-buck'

data = open('bitmoji.png', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=env1,
    aws_secret_access_key=env2,
    config=Config(signature_version='s3v4')
)
s3.Bucket(env3).put_object(Key='bitmoji.png', Body=data)

print ("Done")
