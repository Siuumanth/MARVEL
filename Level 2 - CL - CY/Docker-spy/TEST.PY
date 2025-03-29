import requests

UPLOAD_URL = "http://<publicIP>:5000/upload"
TEST_FILE = "My resume.jpg"  # Replace with an actual image path

try:
    with open(TEST_FILE, "rb") as file:
        files = {"file": (TEST_FILE, file, "image/jpeg")}
        response = requests.post(UPLOAD_URL, files=files)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

except Exception as e:
    print("Error:", e)
