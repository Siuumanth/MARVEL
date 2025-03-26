## What is docker?

Docker is a powerful tool used for developing, packaging, and deploying applications efficiently. Docker is a container management service. Docker was released in 2013. It is open-source and available for different platforms like Windows, macOS, and Linux. Docker is quickly shipping, testing, and deploying code.

So that it reduces your delay between writing code and running it in production. You can create self-contained environments known as containers. That can run consistently on different platforms.

## But what is it?

Docker is a set of Platforms as a service (PaaS) products that use Operating system-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries, and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating system kernel and therefore use fewer resources than a virtual machine.

[article link.](https://www.geeksforgeeks.org/introduction-to-docker/)

[Docker](https://www.geeksforgeeks.org/introduction-to-docker/) is an open-source [containerization](https://www.geeksforgeeks.org/containerization-using-docker/) platform by which you can pack your application and all its dependencies into a standardized unit called a container. Containers are light in weight which makes them portable and they are isolated from the underlying infrastructure and from each other container. You can run the [docker image](https://www.geeksforgeeks.org/what-is-docker-image/) as a [docker container](https://www.geeksforgeeks.org/virtualisation-with-docker-containers/) in any machine where docker is installed without depending on the [operating system.](https://www.geeksforgeeks.org/what-is-an-operating-system/)

## Key Components of Docker

The following are the some of the key components of Docker:

- ****Docker Engine:**** It is a core part of docker, that handles the creation and management of containers.
- ****Docker Image:**** A **Docker image** is a **lightweight, standalone package** that contains everything needed to run an application, including code, runtime, libraries, and dependencies. It acts as a **blueprint** for creating Docker containers. 🚀
- ****Docker Hub:**** It is a cloud based repository that is used for finding and sharing the container images.
- ****Dockerfile:**** It is a script that containing instructions to build a docker image.
- ****Docker Registry**** : It is a storage distribution system for docker images, where you can store the images in both public and private modes.


**Docker images** are like **templates** or **blueprints**, and **containers** are the **running instances** created from those images. You can create multiple containers from the same image, and each runs independently. 🚀

## What is a Dockerfile?

The [Dockerfile](https://www.geeksforgeeks.org/what-is-dockerfile/) uses DSL (Domain Specific Language) and contains instructions for generating a Docker image. Dockerfile will define the processes to quickly produce an image. While creating your application, you should create a Dockerfile in order since the ****Docker daemon**** runs all of the instructions from top to bottom.

- It is a text document that contains necessary commands which on execution help assemble a Docker Image.
- Docker image is created using a Dockerfile.

![umm](https://media.geeksforgeeks.org/wp-content/uploads/20230406105935/dockerfile-2.png)


(The Docker daemon, often referred to simply as “Docker,” is a background service that manages Docker containers on a system.)

### **Virtual Machines (VMs) vs. Containers – Key Differences**

| Feature            | Virtual Machine (VM)                  | Container                                    |
| ------------------ | ------------------------------------- | -------------------------------------------- |
| **Isolation**      | Full OS per VM (strong isolation)     | Shares host OS (lightweight)                 |
| **Startup Time**   | Slow (minutes)                        | Fast (seconds)                               |
| **Size**           | Large (GBs)                           | Small (MBs)                                  |
| **Performance**    | More overhead (runs full OS)          | Near-native performance                      |
| **Resource Usage** | Needs more CPU/RAM                    | Efficient, low resource use                  |
| **Portability**    | Less portable (depends on hypervisor) | Highly portable (works anywhere with Docker) |
| **Use Case**       | Running multiple OSs, legacy apps     | Microservices, lightweight apps              |