import os
import boto3
import requests
from boto3.session import Session
# Set the below variables to use Boto3
aws_access_key_ID = 'xxxxx'
aws_secret_key = 'xxxxx'
api_url = 'https://g3b0zrn210.execute-api.us-east-1.amazonaws.com/dev/ece1724/'

def s3_upload(file_name, bucket_name='ece1724',bucket_file='botosample6.png'):   
    s3_client = boto3.client('s3',aws_access_key_id=aws_access_key_ID, aws_secret_access_key=aws_secret_key )     
    response=s3_client.upload_file(file_name,bucket_name,bucket_file)
    print(response)
    # print(file_name,'uploaded on bucket',bucket_name,'successfully')

def s3_download(file_name, bucket_name='ece1724',bucket_file='botosample4.png'):  
    s3_client = boto3.client('s3',aws_access_key_id=aws_access_key_ID, aws_secret_access_key=aws_secret_key )      
    s3_client.download_file(bucket_name,bucket_file,file_name)


def s3_delete(bucket_file):
    # s3_client = boto3.client('s3',aws_access_key_id=aws_access_key_ID, aws_secret_access_key=aws_secret_key )
    session = Session(aws_access_key_id=aws_access_key_ID,aws_secret_access_key=aws_secret_key)
    s3_resource = session.resource('s3')
    my_bucket = s3_resource.Bucket("ece1724")

    my_bucket.delete_objects(Delete={'Objects': [{'Key': bucket_file}]})

def file_put(file_name, bucket_file):
    url=api_url+bucket_file
    path = os.path.join('upload', file_name)
    # payload = open(f'upload/{file_name}','rb')
    payload = open(path,'rb')

    if file_name.split('.')[-1] == 'png':
        content='image/png'
    if file_name.split('.')[-1]== 'jpeg':
        content='image/jpeg'
    if file_name.split('.')[-1]== 'txt':
        content='text/plain'
    if file_name.split('.')[-1]== 'pdf':
        content='application/pdf'    

    response = requests.request("PUT", url, headers={'Content-Type': content}, data=payload)
    print(response.status_code)

def file_get(file_name, bucket_file):
    url=api_url+bucket_file
    response = requests.get(url)
    path = os.path.join('download', file_name)
    #saving the file
    with open(path, "wb") as file:
        file.write(response.content)

    print(response.status_code)

# s3_upload(file_name=file_name, bucket_file='test1.png')
# # s3_download(file_name='test1_download.png', bucket_file='test1.png')
# s3_delete('test1.png')
file_put(file_name='text1.txt', bucket_file='upload2.txt')
file_get(file_name='download2.txt', bucket_file='upload2.txt')
