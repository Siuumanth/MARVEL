# TASK 1: AWS Lambda

Since this is my first time getting into Amazon Web Services (AWS), I started my learning the fundamentals of Cloud Computing with AWS before I went ahead with this task. I first learnt about the AWS console, then gained knowledge about core services like EC2 instances, Dynamo DB, S3 buckets, etc. Next I went on to learning serverless computing with AWS lambda.
### **Serverless with AWS**
It sounds like there are no servers, but it just means that you don't have to **manage servers**—AWS, GCP or any cloud service will handle them for us. We just write our code normally and it runs **only when it is needed**, responding to events. AWS automatically manages the infrastructure, scaling, and execution of our defined functions in response to triggers.
**FaaS or Function as a Service**  is a part of serverless architecture. It is a way to achieve it, by breaking our apps into small, independent functions, that run only when triggered. We pay only when we use it.
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


After this, I created a simple Express JS server, that serves a simple HTML page. I then connected the script with the HTML, which was capable of testing 3 tasks, opening, closing connection and sending a message, which worked well.

![umm](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/1-webs.png?raw=true)

[Github link](https://github.com/Siuumanth/MARVEL-tasks/tree/main/Level-2-/AWS/AWS-ChatApp/Chat-app)

---
# TASK 2: CI/CD (Continuous Integration & Continuous Delivery) - Intro to Jenkins

I first familiarized myself with the knowledge of DevOps, how it improves the software development process. I also learnt about the traditional methods like Waterfall Model, Agile model, and how DevOps can drastically increase the efficiency of a software development cycle. Then, I moved on to learning about CI/CD, a key aspect of DevOps which automates and accelerates the software development lifecycle, reducing the time required to build a product.

- **Continuous Integration (CI)** ensures that whenever developers make changes to the code, these changes are automatically merged into a shared repository, built, and tested to identify issues early.

- **Continuous Deployment (CD)** automates the release process, pushing changes to production automatically after passing all tests, while **Continuous Delivery** prepares the code for deployment but requires manual approval to push it live. 

## CI/CD with Jenkins:
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

# TASK 4: Terraform

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

# TASK 5: Wireshark

Wireshark is a **network protocol analyzer** used for capturing, inspecting, and analyzing network traffic in real-time. It allows users to see what's happening at a deep level in a network, making it useful for troubleshooting, security analysis, and network optimization.

After setting up, I ran a small Packet Capture (Pcap), where I browsed some website and recorded the packets transferred. I observed the following. I even learnt how to use basic filters to narrow out search space.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-tcp.png?raw=true)

In this normal analysis, we can see the protocols used for each packet, and mainly the flags like `ACK, SYN, SYN-ACK`, whose observations can be crucial for hacking detection. 


![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-http.png?raw=true)

Here some HTTP transfers were made when I accessed an insecure website, and we can see how the packets sent have unencrypted HTML code, concluding that HTTP is insecure. The packets transferred over TLS are more secure because of encryption.

![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-retrans.png?raw=true)

Above, I observed how many packets needed retransmission. A small amount (as shown) would show that our network is stable.


![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/5-graph.png?raw=true)




![](https://github.com/Siuumanth/MARVEL-tasks/blob/main/Level-2-/images/.png?raw=true)


---
## TASK 6: Docker




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