#To use boto3
import boto3
from boto3.session import Session
# Set the below variables to use Boto3
aws_access_key_ID = 'xxxxx'
aws_secret_key = 'xxxxx'
api_url = 'xxxxxx'

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

# s3_upload(file_name=file_name, bucket_file='test1.png')
# s3_download(file_name='test1_download.png', bucket_file='test1.png')
# s3_delete('test1.png')