## Problem statement

Let say a guy is developing a project on his local machine, he sets up all the tools required in his local machine, everything works good. He uploads this code on github and runs the project.

Lets say another guy joins his development team, when he tries to set up by cloning github, he needs to know that what other stuff he needs to install to run the project locally and there is a lot of stuff needed to run that properly. This means ` Extra effort needed to set it up`. And keep in mind that the versions of stuff like `nodejs, mongodb, redis` has to be same to run it properly, and this is very inefficient and time taking. And the effort increases when the other guy is using mac OS, its not possible.

When we have multiple environments, replication of the environment is very hard, which docker solves. 

Also, when we are deploying these versions on the cloud, all the dependencies like 
- node js v16
- mongodb 5
- os
- redis 6, etc

everything needs to be set up on the hosting platform as well, and if we have different virtual machines needs the same setting up, setting it up repeatedly is very time taking.

## How does docker solve this?

We make containers, and we do all of our configuration of OS, dependencies inside the containers, and we share these with our team. This can run in any OS.

These containers are very lightweight, they can very easily be built, shared deployed.

1. Docker daemon
- Responsible for creating containers , puling and pushing images, etc.
2. Docker desktop
- provides us UI to show the state of our PC when containerization takes place and docker runs.  


## Commands:

#### `docker run -it  ubuntu` : 
`-it` means u can interact with that.
initialize ubuntu container, and u will be able to execute commands inside it, like adding stuff, installing libraries and packages.

When it runs:
1. docker runs an ubuntu image, it first checks if your  machine has `ubuntu image`, if u don't, it installs again from docker hub (its a github for containers)


### Images:
They are like mini operating systems with an environment built in. We need containers to run images. Containers are isolated from each other. Many containers can run one image.

### Other Types of Images:

Docker images can be broadly categorized into:
- **Base images** – Minimal OS images like `ubuntu`, `alpine`, or `debian`.
- **Official images** – Maintained by organizations, like `mysql`, `nginx`, or `node`.
    
- **Custom images** – Created by users/developers with their own configurations (e.g., an image with Python and pre-installed libraries).

### Docker commands: 

#### `docker run -it  ubuntu` :
creates an image of ubuntu
- `docker run <image_name>`: runs the image and creates a container
- `docker containers ls` : lists  all open and closed containers on your device.
- `docker ps`: shows all running containers
- 
-  `docker start <container_name>` 
-  `docker stop <container_name>`
starts and stops containers
-  `docker run` 
spins up a new container
- `docker exec <containername> <cmd>`
- `docker exec -it <contname> bash`: opens interactive mode for commands, in bash.
- `docker run -it <image_name>`
- `docker images` - tells what images we have locally

other images types include node js, mysql, nginx, etc.


### What companies do:
So companies build an image out of their project and give u the image to run locally. This image can be pulled and contains all libraries, databases.

## How containers work internally?
>When we run a server in a container, the ports will be locally inside the container, to view it from a website, we should expose the ports.

##### For example, 
lets see it with mailhog/mailhog image

`docker run -it mailhog/mailhog` usually is built to run on  `port 1025:1025`. When we run it, it runs.
When we try to see this server running when we do `localhost:1025`, it does not work as the port address is only inside the container not the whole OS.

Therefore, we need to expose these ports in my computer, for that we need to do:

`docker run -it 8025:8025 -p 1025:1025 mailhog/mailhog`

This will make the ports inside the container 1025 expose on our 1025, same functional as our OS port 1025, same way for 8025.<<>>>>>>

### Lets try for node js:
`docker run -it -p 6000:9000 <application address>` 
This means map the 9000 inside container to the 6000 in my OS. Doing this,  u can expose the ports.

## Dockerising a full Node Js application:

1. Build a node js application and create a `DockerFile`
2. Include a base image (ubuntu), so our app will run on ubuntu, then we install node js in this ubuntu.
### **What is a Dockerfile?**

A **Dockerfile** is a text file that contains instructions to build a **Docker image**. It automates the process of setting up an application environment inside a container.

DockerFile:
```dockerfile
# Use Ubuntu as the base image
FROM ubuntu

# Update package lists to get the latest versions
RUN apt update

# Install curl (a command-line tool for making HTTP requests)
RUN apt-get install -y curl

# Download and execute the Node.js setup script to add Node.js repository
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

# Upgrade all installed packages to the latest versions
RUN apt-get upgrade -y

# Install Node.js and npm (Node Package Manager)
RUN apt-get install -y nodejs

# Copy necessary files for the Node.js application into the container
COPY package.json package.json
COPY package-lock.json package-lock.json
COPY server.js server.js

# Install project dependencies defined in package.json
RUN npm install

# Set the default command to run the Node.js server when the container starts
ENTRYPOINT ["node", "server.js"]

```

To build image:
`docker build -t nginxtest-nodejs .` inside the directory.
Now we have a docker image built.

To run it, we write  
`docker run -it -p 3000:3000 nginxtest-nodejs` 
- as you can see, we include port mapping.

#### Caching layers:
The RUN commands execution are cached, so whenever build runs again, only the copy commands execute, the above ones are cached, so it runs faster.

Everything that is written in dockerfile are in the form of layers, Install layer, RUN layer, COPY layer.

### **Docker Hub – What's the Hype?**

Think of Docker Hub as **GitHub but for Docker images**. It’s a place where you can **store, share, and pull** ready-to-use Docker images.

### **Why Bother Using It?**

✅ **Prebuilt Images** – No need to set up stuff like Node.js, MySQL, etc. Just pull and run.  
✅ **Share Your Own Images** – Push your projects and let others use them.  
✅ **Automated Builds** – Keeps your images up to date.  
✅ **Private Repos** – Store stuff securely if you don’t want the world to see it.  
✅ **Works with Cloud & Kubernetes** – Easy deployment, no drama.


### **Docker Compose – What's the Deal?**

Docker Compose lets you **run multiple containers** together using a simple **YAML file** (`docker-compose.yml`). Instead of running containers one by one, you just **define everything in one file** and start them all with a single command.

### **Why Use It?**

✅ **Easier Multi-Container Setup** – No need to run multiple `docker run` commands.  
✅ **Consistent Environments** – Works the same on any machine.  
✅ **Defines Networks & Volumes** – Handles connections between containers.  
✅ **One Command to Rule Them All** – `docker-compose up` starts everything in one go.

Basically, if your app has a **backend, database, and frontend**, Docker Compose helps **orchestrate** them easily!

