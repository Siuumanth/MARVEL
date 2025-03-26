### **EC2 Instances in AWS**
Amazon **Elastic Compute Cloud (EC2)** provides **virtual servers (instances)** to run applications in the cloud. EC2 instances come in different **instance types**, optimized for compute, memory, storage, or networking.
#### **Key Features:**
- **Scalability** – Easily launch, stop, or resize instances as needed.
- **Instance Types** – General-purpose, compute-optimized, memory-optimized, storage-optimized, GPU instances, etc.
- **Pricing Models** – On-Demand (pay-as-you-go), Reserved Instances (discounted for long-term use), Spot Instances (cheaper, but can be terminated anytime), and Savings Plans.
- **Security** – Managed using **Security Groups** (firewall rules) and **IAM roles**.
- **Elasticity** – Can be auto-scaled using **Auto Scaling Groups** and managed with **Load Balancers**.

### **1. How to Create an EC2 Instance**

1. Go to the **AWS EC2 Dashboard** → Click **Launch Instance**.
2. Choose an **AMI (Amazon Machine Image)** – This is the OS for your instance (e.g., Ubuntu, Amazon Linux).
3. Select an **Instance Type** – Based on CPU, RAM, and storage needs.
4. Configure **Instance Settings** – Number of instances, IAM role, shutdown behavior, etc.
5. Add **Storage** – Choose EBS volume size and type.
6. Configure **Security Group** – Defines inbound/outbound traffic rules (like allowing SSH on port 22).
7. **Launch Instance** – Download the **.pem key file** for SSH access.
    

### **2. Important Configuration Settings**
- **Instance Type** – Determines performance (e.g., `t2.micro` for free tier, `m5.large` for higher performance).
- **Security Groups** – Controls access; allow SSH (`port 22`), HTTP (`port 80`), HTTPS (`port 443`) if needed.
- **IAM Role** – Grants permissions to interact with other AWS services (S3, DynamoDB, etc.).
- **Elastic IP** – Assigns a static public IP to your instance for stable access.

### **3. Using the PEM File for SSH & Post-SSH Tasks**
- The **.pem file** is a **private key** used for secure SSH access to the instance.
- To SSH into the instance:
    `ssh -i your-key.pem ec2-user@your-instance-ip`
    
    - For Ubuntu: `ubuntu@your-instance-ip`
    - For Amazon Linux: `ec2-user@your-instance-ip`
        
#### **Tasks After SSH-ing Into EC2**
- **Install Software** – `sudo apt install` (Ubuntu) or `sudo yum install` (Amazon Linux).
- **Configure Web Servers** – Set up Nginx, Apache, or deploy applications.
- **Manage Files** – Upload/download files using SCP or SFTP.
- **Run Scripts & Services** – Start/stop applications, run Python scripts, Docker containers, etc.
- **Monitor System** – Check logs, resource usage (`top`, `htop`), and troubleshoot issues.