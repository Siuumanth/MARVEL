# Use the official Python 3.10 image as the base image
FROM python:3.10  

# Set the working directory inside the container to /app
WORKDIR /app  

# Copy all files from the current directory (on host) to /app (inside the container)
COPY . .  

# Install necessary Python packages inside the container
RUN pip install requests watchdog  

# Define the command to run the spyware script when the container starts
CMD ["python", "spyware.py"]  
