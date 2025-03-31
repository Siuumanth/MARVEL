'''
import requests

UPLOAD_URL = "http://<publicIP>:5000/upload"
TEST_FILE = "hi.txt"  

try:
    with open(TEST_FILE, "rb") as file:
        files = {"file": (TEST_FILE, file, "umm")}
        response = requests.post(UPLOAD_URL, files=files)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

except Exception as e:
    print("Error:", e)
'''

import os

print(os.listdir('D:\code\marvel\Level-2-\Docker-spy\Spyware'))