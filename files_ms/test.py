import os
import requests

api_url = 'https://g3b0zrn210.execute-api.us-east-1.amazonaws.com/dev/ece1724/'

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


file_put(file_name='text1.txt', bucket_file='upload2.txt')
file_get(file_name='download2.txt', bucket_file='upload2.txt')