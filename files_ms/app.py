import os, logging, requests, mimetypes, base64
from flask import Flask, request, jsonify
from urllib.parse import quote  # Import the quote function from urllib.parse
app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
api_url = os.getenv('AWS_API_GATEWAY')

def file_put(file, file_name, bucket_file):
    print(file_name, bucket_file)

    url=api_url+bucket_file

    # path = os.path.join('upload', file_name)
    # payload = open(path,'rb')
    mime_type, _ = mimetypes.guess_type(file_name)
    app.logger.debug(mime_type)
    
    
    #     if mime_type in ('image/png', 'image/jpeg', 'image/jpg'):
    #         new_file = 'data:image/' + mime_type.split('/')[1] + ';base64, ' + base64.b64encode(file.read()).decode('utf-8')
    #         # new_file = file
    #     else:
    #         new_file = file
    # else:
    #     return {"success": False, "msg": "File type is not supported"}

    # print(file.read())
    print(url)
    # return mime_type
    if mime_type in ('text/plain', 'application/pdf', 'image/png', 'image/jpeg', 'image/jpg'):
        response = requests.put(url, headers={'Content-Type': mime_type}, data=file['files'])
    else:
        return {"msg": "file type is not supported"}
    
    return url if response.status_code==200 else {"msg": "upload failed"}
    # print(response.status_code)

def file_get(file_name, bucket_file):
    print(file_name, bucket_file)
    url=api_url+bucket_file
    file_type = bucket_file.split(".")[1]
    app.logger.debug(file_type)
    result = requests.get(url)

    if file_type=='text/plain':
        response = result.content.deode('utf8')
    # path = os.path.join('download', file_name)

    #saving the file
    # with open(path, "wb") as file:
    #     file.write(response.content)
    # print(response.status_code)
    app.logger.debug(result)
    app.logger.debug(result.content)
    return response

@app.route('/upload', methods=['POST','PUT'])
def upload_file():
    app.logger.debug(request.files)
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['files']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_name = file.filename
    bucket_file =  file_name
    # file.save(os.path.join('upload', file_name))

    response = file_put(request.files, file_name=file_name, bucket_file=bucket_file)

    return jsonify({'response': response}), 200

@app.route('/download/<file_name>', methods=['GET'])
def download_file(file_name):
    bucket_file = file_name
    response = file_get(file_name=file_name, bucket_file=bucket_file)

    return jsonify({'url': api_url+bucket_file}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5010)
