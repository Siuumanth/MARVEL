## TASK 1: AWS Lambda

I began by exploring the fundamentals of **Cloud Computing with AWS**. I first learnt about the AWS console, then gained knowledge about core services like EC2 instances, Dynamo DB, S3 buckets, etc. Next I went on to serverless computing with AWS lambda.
<br />
### Serverless with AWS
It sounds like there are no servers, but it just means that we don't have to **manage servers**—AWS or any cloud service will handle them for us. We just write our code normally and it runs only when it is needed. **FaaS or Function as a Service**  is a part of serverless architecture. It is a way to achieve it, by breaking our apps into small, independent functions, that run only when triggered. 

### Chat app using AWS Lambda

1. `API Gateway`: First, I created an API gateway for Web Sockets Management, for realtime communication. For the route selection expressions, I wrote 6 which handle:
      - `$connect`: client connection 
      - `$disconnect `: disconnection
      -  `$default`:
      - `setName`: to set your name 
      - `sendPublic`: to send a public message
      - `sendPrivate`: to send a private message
      
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/1-socketfun.png?raw=true)
  
      
2. `Attaching Integrations:` I created a single lambda function which would manage each of the routes using switch case. I wrote the backend code for the chatApp.




Web socket code:

![umm](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/1-code.png?raw=true)


![umm](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/1-webs.png?raw=true)

[Github link](https://github.com/Siuumanth/MARVEL/tree/main/Level-2-/AWS/AWS-ChatApp/Chat-app)

<br />

---


<br />

## TASK 2: CI/CD (Continuous Integration &amp; Continuous Delivery) - Jenkins

I first familiarized myself with the knowledge of DevOps, how it improves the software development process. I also learnt about the traditional methods like Waterfall, Agile model, and how DevOps can drastically increase the efficiency of a software development cycle. Then, I moved on to CI/CD:

- **Continuous Integration (CI)** ensures that whenever developers make changes to the code, these changes are automatically merged into a shared repository, built, and tested to identify issues early.

- **Continuous Deployment (CD)** automates the release process, pushing changes to production automatically after passing all tests, while **Continuous Delivery** prepares the code for deployment but requires manual approval to push it live. 
### CI/CD with Jenkins:
Jenkins is an automation platform that allows you to **build, test, and deploy** software using pipelines. It is widely used in CI/CD to streamline the software development process. 

I first familiarized myself with the Jenkins UI and learnt how to `create and scheduling jobs, logging, running jobs, managing teams, etc.`  I tested it on a simple Java application. The setup was able to pull the code from Github, and run tests to get an output and log it.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/2-sum.png?raw=true)

I then went ahead and created a pipeline for testing a simple node js application. The steps were:
- pulling code from Github
- installing dependencies
- run tests defined in package.json 
- run the server 

Pipeline:
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/2-jfile.png?raw=true)
Jenkins console output:
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/2-jlogs.png?raw=true)


[Link to code](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/Jenkins/jenTest)
<br />

---


<br />

## TASK 3: SSH
SSH, or Secure Shell, is a network protocol that enables secure remote access to computers and servers, encrypting data and authentication to ensure secure communication over an unsecured network. The SSH connection works by `public key cryptography`, and is initiated by the client. Once authorized, the public key of the client is stored in the `authorized_keys` file of the server, which contains a list of public keys of machine who are authorized for SSH.
<br />
<br />
For this task, I learnt how SSH works, and how keys are generated and stored in the client and server. I first verified the existence of these keys on my local machine, in the `.ssh` folder and also on an `EC2 instance on AWS.` After this I wrote a script to SSH into the EC2 server, that finds the `authorized_keys` inside the server, and then uploads a copy to the flask server, that I hosted on an EC2 instance.

bash script:
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/3-bash2.png?raw=true)

With this script, which was able to complete the task.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/3-running.png?raw=true)
<br />

---


<br />

## TASK 4: Terraform

**Terraform** is an open-source Infrastructure as Code (IaC) tool, used to define, provision, and manage cloud infrastructure efficiently. It allows users to write declarative configuration files specifying the desired state of infrastructure, and Terraform handles the deployment and changes.
<br />
<br />
I first learnt how to create and configure EC2 instances, DynamoDB, IGWs, routes etc. manually in AWS to get a clearer image of what processes I can automate. I then went ahead learning to learn HCL syntax, basic TF commands and `create, destroy and configure an EC2 instance using terraform`, which was successful.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/4-apply.png?raw=true)

I then went deeper, to create a whole EC2 infrastructure that included:

1. `Virtual Private Network (VPC):` as a secure network for my application.
2. `Internet Gateway`: to allow my VPC to send and receive internet traffic.
3. `Custom route table:` to control how traffic flows within the VPC.
4. `Subnet` which we will use.
5. `Association of subnet to our table`
6. `Security group`: for a firewall and to allow specific ports, 22-SSH, 80-HTTP and 443-HTTPS for connections.
7. `Network Interface`: to create a Virtual Network Adapter.
8. `Elastic IP`: to make sure the public IP remains same even after restart.
9. `EC2 instance`: I attached it to the `network interface` and wrote a script to install dependencies.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/4-code.png?raw=true)
[Full code](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/Terraform/main.tf)
<br />

---


<br />

## TASK 5: Wireshark

Wireshark is a **network protocol analyzer** used for capturing, inspecting, and analyzing network traffic in real-time. It allows users to see what's happening at a deep level in a network, making it useful for troubleshooting, security analysis, and network optimization.
<br />
After setting up, I ran a small Packet Capture (Pcap), where I browsed some websites and recorded the packets transferred. I observed the following. 

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/5-tcp.png?raw=true)

In this normal analysis, we can see the protocols used for each packet, and mainly the flags like `ACK, SYN, SYN-ACK`, whose observations can be crucial for hacking detection. 


![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/5-http.png?raw=true)

Here, some HTTP transfers were made when I accessed an insecure website. We can see how the packets sent have unencrypted HTML code, concluding that HTTP is insecure, whereas, packets transferred over TLS are encrypted.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/5-graph.png?raw=true)
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/5-retrans.png?raw=true)

Above, I observed retransmission data. A small amount (as shown) would show that our network is stable. A high amount would indicate packet loss. 

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/5-rtt.png?raw=true)

Round Trip Time (RTT) measures the time it takes for a data packet to travel from a source to a destination and back. Above, our graph is showing a linear decrease of RTT, which shows that our network performance increases overtime

<br />

---


<br />

## TASK 6: Docker

Docker is a tool that use Operating system-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries, and configuration files, they can communicate with each other through well-defined channels.
<br />
A **Docker image** is a lightweight, standalone package that contains everything needed to run an application, including code, runtime, libraries, and dependencies. It acts as a blueprint for creating Docker containers. **Dockerfile** is a set of instructions containing the commands for generating a docker image.
<br />
For this task, I first explored the use cases of docker and how it accelerates both the deployment and development process. I then learnt the basic docker commands like `run, build, ps, start, exec, etc.` For the practical experience, then created a simple Nodejs server application and dockerized that to create its image.

dockerfile:
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/6-dockerfile.png?raw=true)
I then built the image, and ran the image. Using port mapping, I was able to host the server inside the container, and make it visible in my Windows machine.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/6-container.png?raw=true)

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/6-running.png?raw=true)

<br />

---


<br />


## TASK 7: Docker File Spyware

Spyware is a type of malicious software designed to secretly monitor and collect information from a system without the user's consent. It can track activities, steal sensitive data, or send collected information to a remote server.  Docker can be used to containerize the spyware code and bypass security restrictions while operating in a sandboxed environment.

I first wrote a simple spyware code in python that monitors a folder for any new files, and coded a simple flask server where I can upload files as POST requests, which accepts the files and stores it in a local folder.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/7-code2.png?raw=true)

To enable remote access, I decided to enhance my skills and host the server on an EC2 instance. For this I created one, using SSH I gained access into the machine and created my server files there, and hosted it.

I then containerized my spyware code, using a python image.
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/7-dfile.png?raw=true)
Finally, I built an image and ran a container, where I used file mounting to monitor a folder outside of the container, i.e, a windows folder, and I was successfully able to monitor the folder and upload the files to my EC2 machine.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/7-working.png?raw=true)

[Github link](https://github.com/Siuumanth/MARVEL/tree/main/Level-2-/Docker-spy/Spyware)
<br />

---


<br />

## TASK 8: Web Scraping and Automation

Selenium is a tool used for **automated testing** of web applications, but it can also be used for tasks like web scraping and browser automation. Selenium works by sending commands to a web browser, instructing it to perform tasks like clicking a button, entering text in a form, or navigating through a page.

For this task, I ran tests in 2 websites, `expedia and skyscanner`, which didn't work too well. Then, I tried on `Google flights`, which after hours of testing, seemed perfect, because of its easy UI.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/8-WIP.png?raw=true)

Identifying the proper IDs of elements was a hassle. I faced issues even if I had the correct ID. I finally figured out a way and was able to automate the navigation and scraping.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/8-final.png?raw=true)

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/8-table.png?raw=true)

[Github Link](https://github.com/Siuumanth/MARVEL/tree/main/Level-2-/Selenium/practical)
<br />

---


<br />

## TASK 9: Hashing

Hashing is the practice of converting a string of characters, to another value for security. This is mainly done for classified details like passwords in databases. The algorithm `sha256` can be used to hash a string, in a way that the change cannot be reversed, and every particular string gives the same hashed value. 
<br /><br />
For this task I used a python's `hashlib`, and built a simple flask server, which hosted a basic login/signup page. The password would then be hashed using the `sha256` algorithm, and stored in a local database. 

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/9-login.png?raw=true)

When the login details are entered, the code would then apply the same hash function on submitted password, and verify the details with the stored info.

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/9-db.png?raw=true)

As we can see here, all the passwords stored are hashed.
[Github](https://github.com/Siuumanth/MARVEL/tree/main/Level-2-/hashing)
<br />

---


<br />

## TASK 10: NMap

Nmap is a powerful network discovery tool that can be used for :
- IP/Port scanning
- discovery of services
- OS detection, Version detection
- information on targets, including reverse DNS
- identifying device types and MAC addresses.

I first learnt about how SYN scans work, and the various options in the NMAP commands and flags like `-sS , -sP , -A , -Pn , -iL , -6 , -sn , -p and more`. I then moved on to analysis.

Identifying devices:
![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/10-all.png?raw=true)
#### Conclusions:
My network had 6 devices connected to it, which were responsive when I ran an `agressive scan`, I recorded the observations:
1. In a SYN scan, some devices had firewall enables, and Nmap was not able to bypass that to get the required information.
2. My router had some services running like Telnet, DNS, HTTPS. 
3. It also had an expired SSL certificate which might make it vulnerable to brute force attacks.

Scanning a website [scanme.org]

![](https://github.com/Siuumanth/MARVEL/blob/main/Level-2-/images/10-scanme.png?raw=true)

Here, we can see:
1. DNS in action.
2. OpenSSH running on Ubuntu, and its versions which can be exploited.
3. Web server with an open insecure HTTP port. The version is older,which can make it vulnerable.

I even scanned my AWS EC2 instance, where I verified the OS running and ports enabled.



<br />

---



<br />

[Detailed notes on all tasks](https://github.com/Siuumanth/MARVEL/tree/main/Level-2-)

<br />




