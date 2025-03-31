# **Level 3 - CL - CY Report**

---
## TASK 1: AWS Lambda

Since this is my first time getting into Amazon Web Services (AWS), I started my learning the fundamentals of Cloud Computing with AWS before I went ahead with this task. I first learnt about the AWS console, then gained knowledge about core services like EC2 instances, Dynamo DB, S3 buckets, etc. Next I went on to learning serverless computing with AWS lambda.
### **Serverless with AWS**
It sounds like there are no servers, but it just means that you don't have to **manage servers**—AWS, GCP or any cloud service will handle them for us. We just write our code normally and it runs **only when it is needed**. **FaaS or Function as a Service**  is a part of serverless architecture. It is a way to achieve it, by breaking our apps into small, independent functions, that run only when triggered. 
### **AWS Lambda**
It is the **FaaS platform of AWS**. We can define a function, upload it and AWS runs when its triggered. To get started, I followed the AWS' official tutorial on creating a simple "Hello World" function for testing. Next, I went ahead creating the Chat App.

1. `API Gateway`: First, I created an API gateway for Web Sockets Management, for realtime communication. For the route selection expressions, I chose the 3 basic ones which handle:
      - `$connect route`: client connection 
      - `$disconnect route`: disconnection
      -  `$default route`: message sharing
      
2. `Attaching Integrations:` I created 3 lambda functions to manage each of the above routes, and linked them. After these steps, I got the WebSocket URL which I could then integrate with my app. 

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/1-socketfun.png?raw=true)


Code for web socket:

![umm](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/1-code.png?raw=true)


![umm](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/1-webs.png?raw=true)

[Github link](https://github.com/Siuumanth/MARVEL-tasks/tree/main/Level-2-/AWS/AWS-ChatApp/Chat-app)

---
## TASK 2: CI/CD (Continuous Integration & Continuous Delivery) - Intro to Jenkins

I first familiarized myself with the knowledge of DevOps, how it improves the software development process. I also learnt about the traditional methods like Waterfall Model, Agile model, and how DevOps can drastically increase the efficiency of a software development cycle. Then, I moved on to learning about CI/CD, a key aspect of DevOps which automates and accelerates the software development lifecycle, reducing the time required to build a product.

- **Continuous Integration (CI)** ensures that whenever developers make changes to the code, these changes are automatically merged into a shared repository, built, and tested to identify issues early.

- **Continuous Deployment (CD)** automates the release process, pushing changes to production automatically after passing all tests, while **Continuous Delivery** prepares the code for deployment but requires manual approval to push it live. 

### CI/CD with Jenkins:
Jenkins is an **automation platform** that allows you to **build, test, and deploy** software using pipelines. It is widely used in **Continuous Integration (CI) and Continuous Deployment (CD)** to streamline the software development process. 

I first familiarized myself with the Jenkins UI and learnt how to create and scheduling jobs, logging, running jobs, managing teams, etc.  I tested it on a simple Java application. The setup was able to pull the code from Github, and run tests to get an output and log it.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/2-sum.png?raw=true)

I then went ahead and created a pipeline for testing a simple node js application. The steps were:
- pulling code from github
- installing dependencies
- run tests defined in package.json (none for now)
- run the server and make sure no error occurs.

Pipeline:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/2-jfile.png?raw=true)
Jenkins console output:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/2-jlogs.png?raw=true)


[Link to code](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/Jenkins/jenTest)

---
## TASK 3: SSH
SSH, or Secure Shell, is a network protocol that enables secure remote access to computers and servers, encrypting data and authentication to ensure secure communication over an unsecured network. The SSH connection works by `public key cryptography`, and is initiated by the client. Once authorized, the public key of the client is stored in the `authorized_keys` file of the server, which contains a list of public keys of machine who are authorized for SSH.
The communication then takes place by: 

For this task, I learnt how SSH works, and how keys are generated and stored in the client and server. I first verified the existence of these keys on my local machine, in the `.ssh` folder and also on an `EC2 instance on AWS.` After this I wrote a script to SSH into the EC2 server (I used the `.pem` keys for authorization since there is no other way), that finds the `authorized_keys` file inside the server, and then uploads a copy of that file to another server, that I hosted on an EC2 instance.

bash script:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/3-bash.png?raw=true)

I then ran this script, which was able to complete the stated task.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/3-running.png?raw=true)





---
## TASK 4: Terraform

**Terraform** is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp, used to define, provision, and manage cloud infrastructure efficiently. It allows users to write declarative configuration files specifying the desired state of infrastructure (like servers, networks, and databases), and Terraform handles the deployment and changes.

I first learnt how to create and configure EC2 instances, DynamoDB, IGWs, routes etc. manually in AWS to get a clearer image of what processes I can automate. I then went ahead learning to learn HCL syntax, basic TF commands and create, destroy and configure an EC2 instance using terraform, which was successful.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/4-apply.png?raw=true)

I then went deeper, to create a whole EC2 infrastructure that included:

1. `Virtual Private Network (VPC):` to create a secure network for my application.
2. `Internet Gateway`: to allow my VPC to send and receive traffic from the internet.
3. `Custom route table:` to control how traffic flows within the VPC.
4. `Subnet` which we will use.
5. `Association of subnet to our table`
6. `Security group`: for a firewall and to allow specific ports, 22-SSH, 80-HTTP and 443-HTTPS for connections.
7. `Network Interface`: to create a Virtual Network Adapter.
8. `Elastic IP`: to make sure the public IP remains same even after restart.
9. `EC2 instance`: where I attached it to the `network interface` and wrote a script to install recent dependencies and Apache.

Code snippet:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/4-code.png?raw=true)
[Full code](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/Terraform/main.tf)

---

## TASK 5: Wireshark

Wireshark is a **network protocol analyzer** used for capturing, inspecting, and analyzing network traffic in real-time. It allows users to see what's happening at a deep level in a network, making it useful for troubleshooting, security analysis, and network optimization.

After setting up, I ran a small Packet Capture (Pcap), where I browsed some website and recorded the packets transferred. I observed the following. I even learnt how to use basic filters to narrow out search space.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-tcp.png?raw=true)

In this normal analysis, we can see the protocols used for each packet, and mainly the flags like `ACK, SYN, SYN-ACK`, whose observations can be crucial for hacking detection. 


![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-http.png?raw=true)

Here some HTTP transfers were made when I accessed an insecure website, and we can see how the packets sent have unencrypted HTML code, concluding that HTTP is insecure. The packets transferred over TLS are more secure because of encryption.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-graph.png?raw=true)
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-retrans.png?raw=true)

Above, I observed how many packets needed retransmission. A small amount (as shown) would show that our network is stable. A high amount would indicate packet loss. This can help us discover network bottlenecks, performance.


![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-rtt.png?raw=true)
Round Trip Time (RTT) measures the time it takes for a data packet to travel from a source to a destination and back, serving as a key indicator of network latency and connection quality. Above, our graph is showing a linear decrease of RTT, which shows that out network performance increases overtime

---
## TASK 6: Docker

Docker is a set of Platforms as a service (PaaS) products that use Operating system-level virtualization to deliver software in packages called containers. **Containers** are isolated from one another and bundle their own software, libraries, and configuration files, they can communicate with each other through well-defined channels.

A **Docker image** is a lightweight, standalone package that contains everything needed to run an application, including code, runtime, libraries, and dependencies. It acts as a blueprint for creating Docker containers . Containers are the **running instances** created from those images.
**Dockerfile** is a set of instructions containing the necessary commands for generating a docker image.

For this task, I first explored the use cases of docker and how it accelerates both the deployment and development process. I then learnt the basic docker commands like `run, build, ps, start, exec, etc.` For the practical experience, then created a simple Nodejs server application and dockerized that to create its image.

dockerfile:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/6-dockerfile.png?raw=true)
I then built the image, and ran the image. Using port mapping, I was able to host the server inside the container, and make it visible in my Windows machine.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/6-container.png?raw=true)

Running the image:
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/6-running.png?raw=true)

---

## TASK 7: Docker File Spyware

Spyware is a type of malicious software designed to secretly monitor and collect information from a system without the user's consent. It can track activities, steal sensitive data, or send collected information to a remote server. 
Docker can be used to containerize the spyware code and bypass security restrictions while operating in a sandboxed environment.

I first wrote a simple spyware code in python that monitors a folder for any new files, and coded a simple flask server where I can upload files as `POST` requests, which takes the files and stores it in a local folder.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/7-code2.png?raw=true)

To enable remote access, I decided to enhance my skills and host the server on an EC2 instance. For this I created one, using SSH I gained access into the machine and created my server files there, and hosted it.

I then containerized my spyware code, using a python image.
![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/7-dfile.png?raw=true)
Finally, I built an image and ran a container, where I used file mounting to monitor a folder outside of the container, i.e, a windows folder, and I was successfully able to monitor the folder and upload the files to my EC2 machine.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/7-working.png?raw=true)

[Github link](https://github.com/Siuumanth/MARVEL-tasks/tree/main/Level-2-/Docker-spy/Spyware)

---

## TASK 8: Web Scraping and Automation

Selenium is an **open-source framework** for automating web browsers. It is primarily used for **automated testing** of web applications, but it can also be used for tasks like web scraping and browser automation. Selenium works by sending commands to a web browser, instructing it to perform tasks like clicking a button, entering text in a form, or navigating through a page.

For this task, I ran tests in 2 websites, `expedia and skyscanner`, which didn't work too well. Then, I tried on `Google flights`, which after hours of testing, seemed perfect, because of its easy UI.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/8-WIP.png?raw=true)

Identifying the proper IDs of elements in the website, was a hassle, and I faced issues even if i got the correct ID. I finally figured out a way and was able to automate the navigation and scraping.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/8-final.png?raw=true)

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/8-table.png?raw=true)

Final `.csv` file of the scraped flight details data.

[Github Link](https://github.com/Siuumanth/MARVEL-tasks/tree/main/Level-2-/Selenium/practical)

---

## TASK 9: Hashing

Hashing is the practice of converting a string of characters, to another value for security. This is mainly done for classified details like passwords in databases. The algorithm `sha256` can be used to hash a string, in a way that the change cannot be reversed, and every particular string gives the same hashed value. 

For this task I used a python's `hashlib`, and built a simple flask server, which hosted a basic login/signup page. The password would then be hashed using the `sha256` algorithm, and stored in a local database. 

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/9-login.png?raw=true)

When the login details are entered, the code would then apply the same hash function on submitted password, and verify the details with the stored info.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/9-db.png?raw=true)

As we can see here, all the passwords stored are hashed.
[Github](https://github.com/Siuumanth/MARVEL-tasks/tree/main/Level-2-/hashing)

---
## TASK 10: NMap

Nmap is a powerful network discovery tool that can be used for :
- IP/Port scanning
- discovery of services
- OS detection, Version detection
- information on targets, including reverse DNS
- identifying device types and MAC addresses.

I first learnt about how SYN scans work, and the various options in the NMAP commands like `-sS , -sP , -A , -Pn , -iL , -6 , -sn , -p and more`. I was facing issues with using NMAP, which I was able to resolve by changing the network settings in Virtual Box from `NAT` to `Bridged Adapter` . I ran NMAP on my network. I was able to identify all the devices that was connected to my network, and also on another website specifically made for pentesting.


I saw resources on how we can find vulnerabilities when we get an NMAP result, identifying the different types of ports, and basics on how we can exploit those vulnerabilities, like SSH or FTP, but I was not able to fully exploit them.

Identifying devices :

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/6-normal_scan.png?raw=true)

Identifying Ports :

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/6-ports.png?raw=true)

Scanning a website ([scanme.org](scanme.org))
  
![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/6-scanme.png?raw=true)




<br>