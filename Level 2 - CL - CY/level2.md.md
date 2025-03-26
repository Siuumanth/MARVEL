
## TASK 2: CI/CD (Continuous Integration & Continuous Delivery) - Intro to Jenkins

### CI / CD :
CI/CD stands for **Continuous Integration and Continuous Deployment/Delivery**, a practice in software development aimed at automating the process of building, testing, and deploying code changes. 

- **Continuous Integration (CI)** ensures that whenever developers make changes to the code, these changes are automatically merged into a shared repository, built, and tested to identify issues early.

- **Continuous Deployment (CD)** automates the release process, pushing changes to production automatically after passing all tests, while **Continuous Delivery** prepares the code for deployment but requires manual approval to push it live. 


## TASK 4: Terraform

**Terraform** is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp, used to define, provision, and manage cloud infrastructure efficiently. It allows users to write declarative configuration files specifying the desired state of infrastructure (like servers, networks, and databases), and Terraform handles the deployment and changes.

It supports multiple cloud providers like AWS, Azure, and GCP, as well as on-premises systems, making it a versatile tool for automating and maintaining consistent infrastructure across environments.


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