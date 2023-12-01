import os, logging, requests, mimetypes
from flask import Flask, request, jsonify
from urllib.parse import quote  # Import the quote function from urllib.parse
app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
api_url = os.getenv('AWS_API_GATEWAY')

def file_put(file_name, bucket_file):
    print(file_name, bucket_file)

    url=api_url+bucket_file
    path = os.path.join('upload', file_name)
    payload = open(path,'rb')
    mime_type, _ = mimetypes.guess_type(file_name)
    content = mime_type if mime_type else 'application/octet-stream'
    response = requests.request("PUT", url, headers={'Content-Type': content}, data=payload)
    # print(response.status_code)

def file_get(file_name, bucket_file):
    print(file_name, bucket_file)
    url=api_url+bucket_file
    response = requests.get(url)
    # path = os.path.join('download', file_name)

    #saving the file
    # with open(path, "wb") as file:
    #     file.write(response.content)
    # print(response.status_code)
    app.logger.debug(response)
    app.logger.debug(response.content)
    return response

@app.route('/upload', methods=['POST','PUT'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_name = file.filename
    bucket_file =  file_name
    file.save(os.path.join('upload', file_name))

    file_put(file_name=file_name, bucket_file=bucket_file)

    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download/<file_name>', methods=['GET'])
def download_file(file_name):
    bucket_file = file_name
    file_get(file_name=file_name, bucket_file=bucket_file)

    return jsonify({'message': 'File downloaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5010)
