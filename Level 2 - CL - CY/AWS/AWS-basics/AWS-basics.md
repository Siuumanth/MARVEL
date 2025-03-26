### **What is AWS?**

**Amazon Web Services (AWS)** is the world’s most popular **cloud computing platform**, offering **on-demand computing resources** like servers, storage, databases, and networking—all available over the internet. Instead of maintaining physical servers, companies use AWS to **rent computing power** and scale their infrastructure as needed.
### **Why AWS?**
✅ **No upfront cost** – Pay only for what you use.  
✅ **Highly scalable** – Can handle small to massive workloads.  
✅ **Global infrastructure** – Data centers worldwide for low latency.  
✅ **Security & reliability** – AWS manages security, backups, and maintenance.
### **AWS Provides Three Main Services:**
1. **Compute** – Virtual machines (EC2), serverless (Lambda), containers (ECS, EKS).
2. **Storage** – S3 (object storage), EBS (disk storage), EFS (file storage).
3. **Databases** – RDS (SQL), DynamoDB (NoSQL), Aurora, Redshift.

💡 AWS is used by startups, enterprises, and even individuals to **host applications, process data, and build scalable architectures**. Terraform helps automate and manage AWS infrastructure efficiently.


# **Getting started**

# **1. EC2 (Elastic Compute Cloud) – Virtual Machines on AWS**

### **What is EC2?**
EC2 (Elastic Compute Cloud) is a service that provides **virtual machines** (called instances) in the cloud. Instead of maintaining physical servers, AWS allows you to create, configure, and run virtual machines based on your needs.
### **Key Concepts:**
- **AMI (Amazon Machine Image):** A template that contains an operating system (e.g., Ubuntu, Windows) and software configurations for launching instances.
- **Instance Types:** Different configurations of CPU, RAM, and network performance (e.g., `t2.micro`, `m5.large`).
- **Security Groups:** Act like a firewall, controlling inbound and outbound traffic to instances.
- **Key Pairs:** Used for authentication when connecting to an EC2 instance via SSH.
- **Elastic IP:** A static public IP that can be assigned to an EC2 instance.
    
### **Use Cases:**

✅ Hosting websites and applications.  
✅ Running backend services, databases, and APIs.  
✅ Processing large-scale computations (e.g., machine learning models).

---

# **2. S3 (Simple Storage Service) – Object Storage**

### **What is S3?**

S3 (Simple Storage Service) is a cloud storage service that lets you store and retrieve **any type of file** (documents, images, videos, backups, etc.).

### **Key Concepts:**
- **Buckets:** Like a folder where files are stored (globally unique names).
- **Objects:** The actual files inside a bucket.
- **Storage Classes:** Different pricing based on access frequency:
    - **Standard:** Frequently accessed data.
    - **Infrequent Access (IA):** Lower cost, but retrieval fees apply.
    - **Glacier:** Cheapest but for long-term archival storage.
        
- **Versioning:** Keeps previous versions of a file in case of accidental deletion.
- **Public vs. Private Access:** By default, all files in S3 are private unless made public.
    
### **Use Cases:**

✅ Storing website assets (images, CSS, JS).  
✅ Backing up and archiving data.  
✅ Hosting static websites.

---

# **3. DynamoDB – NoSQL Database**

### **What is DynamoDB?**
DynamoDB is a **fully managed NoSQL database** designed for fast and scalable key-value storage. Unlike traditional relational databases, it does not use tables with rows and columns but instead relies on key-value pairs and JSON-like structures.

### **Key Concepts:**
- **Tables:** Store data, similar to SQL databases.
- **Partition Key (Primary Key):** The unique identifier for an item (e.g., `user_id`).
- **Sort Key (Optional):** Helps sort and filter data within a partition.
- **Read/Write Capacity:** Determines how much data can be read/written per second.
- **On-Demand Mode:** Scales automatically based on traffic without needing manual capacity adjustments.
### **Use Cases:**

✅ Storing real-time user data for applications.  
✅ Managing IoT sensor data and logs.  
✅ Leaderboards and session management in games.

---

# **4. IAM (Identity & Access Management) – Permissions & Roles**

### **What is IAM?**

IAM (Identity and Access Management) is AWS’s service for **controlling access** to AWS resources. It allows you to manage **users, groups, roles, and permissions** to ensure security and prevent unauthorized access.

### **Key Concepts:**
- **IAM Users:** Individual AWS accounts with login credentials.
- **IAM Groups:** A collection of users with the same permissions.
- **IAM Policies:** JSON-based rules that define what actions users can perform (e.g., allow S3 read-only access).
- **IAM Roles:** Used to grant permissions to AWS services instead of individual users.
- **MFA (Multi-Factor Authentication):** Extra security layer requiring a second authentication factor (e.g., mobile OTP).
    
### **Use Cases:**

✅ Restricting access to AWS services based on user roles.  
✅ Giving temporary access to third-party applications.  
✅ Managing permissions for AWS services to interact with each other.

---

# **5. VPC (Virtual Private Cloud) – Networking Basics**

### **What is VPC?**
VPC (Virtual Private Cloud) is AWS’s networking layer that allows you to create **a private, isolated network** for your AWS resources. It works like a **virtual data center** in the cloud.
### **Key Concepts:**
- **CIDR Block:** Defines the IP address range for the VPC (e.g., `10.0.0.0/16`).
- **Subnets:** Divide the VPC into smaller sections, like **public** and **private** subnets.
- **Internet Gateway:** Allows resources in a VPC to connect to the internet.
- **Route Table:** Defines how network traffic is routed within the VPC.
- **NAT Gateway:** Allows private subnet resources to access the internet without exposing them.
### **Use Cases:**

✅ Hosting secure, private applications.  
✅ Isolating sensitive workloads from the internet.  
✅ Creating hybrid cloud environments with on-premises data centers.

---

# **6. AWS CLI (Command Line Interface) – Managing AWS from Terminal**

### **What is AWS CLI?**

AWS CLI (Command Line Interface) is a tool that allows you to **manage AWS services from the terminal** instead of the AWS Console.
### **Key Features:**
- Automate AWS tasks without using the web interface.
- Manage EC2, S3, IAM, and other services with commands.
- Easily integrate AWS operations into scripts.
    
### **Basic AWS CLI Commands:**

- `aws configure` – Set up AWS credentials.
- `aws s3 ls` – List S3 buckets.
- `aws ec2 describe-instances` – Get details of EC2 instances.
- `aws dynamodb list-tables` – Show DynamoDB tables.
### **Use Cases:**

✅ Automating AWS tasks via scripts.  
✅ Managing AWS resources without logging into the console.  
✅ Faster deployments and administration.

---

### **Final Thoughts**

These are some of the **core AWS services** you should know before getting into Terraform. If you want to **practice hands-on**, you can sign up for the **AWS Free Tier** and try these services manually.