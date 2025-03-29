import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "/app/imgs"  # Folder to monitor
UPLOAD_URL = "http://<publicIP>:5000/upload"


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
            time.sleep(1)  # keep the script runing
    except KeyboardInterrupt:
        observer.stop()  # stop monitooring when interupted

    observer.join()  # wait for the obsever to clean up

'''
he Observer runs in a separate background thread, continuously 
monitoring the folder.

Meanwhile, the while True: loop keeps the main thread alive.

When a file is created, watchdog triggers on_created() in the background 
without blocking the main loop.
'''