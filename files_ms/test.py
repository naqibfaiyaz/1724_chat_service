import os
import requests
import mimetypes


api_url = 'https://g3b0zrn210.execute-api.us-east-1.amazonaws.com/dev/ece1724/'

def file_put(file_name, bucket_file):
    url=api_url+bucket_file
    path = os.path.join('upload', file_name)
    payload = open(path,'rb')
    mime_type, _ = mimetypes.guess_type(file_name)
    content = mime_type if mime_type else 'application/octet-stream'
    response = requests.request("PUT", url, headers={'Content-Type': content}, data=payload)
    # print(response.status_code)

def file_get(file_name, bucket_file):
    url=api_url+bucket_file
    response = requests.get(url)
    path = os.path.join('download', file_name)

    #saving the file
    with open(path, "wb") as file:
        file.write(response.content)
    # print(response.status_code)


file_put(file_name='sample_image.png', bucket_file='image1.png')
file_put(file_name='sample_text.txt', bucket_file='text1.txt')
file_put(file_name='sample_pdf.pdf', bucket_file='pdf1.pdf')

file_get(file_name='image_saved.png', bucket_file='image1.png')
file_get(file_name='text_saved.txt', bucket_file='text1.txt')
file_get(file_name='pdf_saved.pdf', bucket_file='pdf1.pdf')