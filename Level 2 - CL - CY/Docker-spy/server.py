from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "D:/code/marvel/Level 2 - CL - CY/Docker-spy/folder"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"File {file.filename} uploaded successfully!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 
