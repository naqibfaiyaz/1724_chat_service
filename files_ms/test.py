import boto3
import requests
from boto3.session import Session
# create client object

aws_access_key_ID = 'AKIAZW3GN2VIUB7VVVPD'
aws_secret_key = 'xXv3oIu58neo5GKHjLj3cMjcNwlANBKENJMugnR4'
file_name = 'files/sample.png'
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


def file_get(file_name, bucket_file='testrest.png'):
    url=api_url+bucket_file
    response = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(response.content)
    print(response.status_code,'\n\n')
    # print(response.json())

def file_put(file_name, bucket_file='testrest.png'):
    url=api_url+file_name
    print(url)
    response = requests.put(url)

    f = open('files/saved1.png', 'rb')
    with open('files/sample.png','rb') as fp:
        file_data = fp.read()

    files = {"file": (file_data)}

    resp = requests.put(url, files)


    print(response.status_code,'\n\n')



                            

# s3_upload(file_name=file_name, bucket_file='test1.png')
# # s3_download(file_name='test1_download.png', bucket_file='test1.png')
# s3_delete('test1.png')
# file_get(file_name='files\saved1.png', bucket_file='testfile2.png')
file_put(file_name='savedfinal.png', bucket_file='testfile20.png')