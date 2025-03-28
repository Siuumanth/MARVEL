## Steps to do:

STEPS:
1. Create a VPC
2. Create Internet Gateway to send data publicly
3. Create Custom Route Table
4. Create a Subnet
5. Associate subnet with Route Table
6. Create Security Group to allow port 22, 80, 443 - 22 is for SSH, 80 and 443 is for HTTP.

7. Create a network interface with an IP in the subnet that was created in step 4
8. Assign an elastic IP to the network interface crearted in step 7
9. Create an Ubuntu server and install/enable apache2  


## Explanation:
### **AWS VPC Setup & EC2 Deployment Steps**

#### **1. Create a VPC**
- A **VPC (Virtual Private Cloud)** is a private network where AWS resources can communicate securely.
- You define a **CIDR block** (e.g., `10.0.0.0/16`) to set the IP range for your VPC.

#### **2. Create an Internet Gateway**
- An **Internet Gateway (IGW)** allows your VPC to send and receive traffic from the internet.
- It must be **attached to the VPC** to enable public access.

#### **3. Create a Custom Route Table**
- A **Route Table** controls how traffic flows within the VPC.
- Add a rule to send all internet-bound traffic (`0.0.0.0/0`) **to the IGW**.

#### **4. Create a Subnet**
- A **subnet** is a smaller network inside the VPC.
- You decide if it should be **public** (accessible from the internet) or **private** (isolated).
- Example: `10.0.1.0/24` for a public subnet.

#### **5. Associate Subnet with Route Table**
- Attach the **public subnet** to the **custom route table**.
- This allows resources in the subnet to use the **IGW** for internet access.

#### **6. Create a Security Group (SG) to Allow Ports 22, 80, 443**
- A **Security Group** acts as a firewall for EC2 instances.
- Open **port 22 (SSH)** for remote login.
- Open **port 80 (HTTP)** and **port 443 (HTTPS)** for web traffic.

#### **7. Create a Network Interface (ENI) in the Subnet**
- A **Network Interface (ENI)** is a virtual network adapter.
- Assign it an **IP address from the subnet** to allow communication.

#### **8. Assign an Elastic IP to the Network Interface**
- An **Elastic IP (EIP)** is a static public IP that doesn’t change.
- It allows your server to be publicly accessible even if restarted.
    
#### **9. Create an Ubuntu Server & Install Apache2**
- Launch an **EC2 instance** with the Ubuntu AMI.
- Attach it to the **network interface**.
- SSH into the server and install Apache.

---

# Actually doing it:

First go to EC2 n get your key pairs. This can enable you to ssh into your VM.

### **What is a CIDR Block?**

A **CIDR (Classless Inter-Domain Routing) block** defines the IP address range for a network. It helps in efficient IP allocation and subnetting.

### **How It Works in AWS VPC?**

When creating a VPC, you specify a **CIDR block** to determine the range of IP addresses available. Example:

- `10.0.0.0/16` → Provides **65,536** IP addresses (`10.0.0.0` to `10.0.255.255`).
- `192.168.1.0/24` → Provides **256** IP addresses (`192.168.1.0` to `192.168.1.255`).

The **suffix (`/16`, `/24`)** represents the number of fixed bits in the network portion, affecting the number of available IPs.
- **Smaller number (e.g., /16) → More IPs**
- **Larger number (e.g., /28) → Fewer IPs**

### **What is Ingress and Egress in Networking?**

- **Ingress** = **Incoming traffic** (data coming **into** a network or resource).
- **Egress** = **Outgoing traffic** (data going **out** of a network or resource).

### **How It Works in AWS?**
In **AWS Security Groups**, you define **Ingress Rules** (what traffic can enter) and **Egress Rules** (what traffic can exit).

#### **Example: Security Group Rules**
- **Ingress Rule:** Allow SSH (port 22) from `0.0.0.0/0` → Lets anyone SSH into the instance.
- **Egress Rule:** Allow `0.0.0.0/0` on all ports → Allows the instance to reach the internet.

By default:
- **Security Groups** **block all ingress** and **allow all egress** unless modified.
- **Network ACLs** provide more granular control and can block both ingress and egress traffic.


Code:
```js
provider "aws" {
}


# STEPS:
# 1. Create a VPC
# 2. Create Internet Gateway to send data to internet publicly
# 3. Create Custom Route Table
# 4. Create a Subnet
# 5. Associate subnet with Route Table
# 6. Create Security Group to allow port 22, 80, 443
# 7. Create a network interface with an IP in the subnet that was created in step 4
# 8. Assign an elastic IP to the network interface crearted in step 7
# 9. Create an Ubuntu server and install/enable apache2
  

# 1. Create a VPC
resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}

# 2. Create Internet Gateway to send data to internet publicly
resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.prod-vpc.id
}
  

# 3. Create Custom Route Table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod-vpc.id

//defining the routes
  route {
    // 0.0.0.0/0 is the defaultt internet route, IPV4
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGW.id
  }
  // IPV6
  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = aws_internet_gateway.IGW.id
  }
  
  tags = {
    Name = "Prod"
  }
}

# 4. Create a Subnet
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.prod-vpc.id
  cidr_block = "10.0.1.0/24"  //the subnet we will use
  tags = {
    Name = "prod-subnet"
  }
}

  
# 5. Associate subnet with Route Table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}

# 6. Create Security Group to allow port 22, 80, 443
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.prod-vpc.id
  //defining ports routes
   ingress {
    description      = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  
    ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
    ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
    egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"  //this means any protocol
    cidr_blocks      = ["0.0.0.0/0"]
  }
  tags = {
      Name = "allow_web"
  }
}


# 7. Create a network interface with an IP in the subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.0.50"]  // any one within the subnet
  security_groups = [aws_security_group.allow_web.id]
  # the above line is to assign the private security group to the network interface  
}

# 8. Assign an elastic IP to the network interface crearted in step 7
# now we will assign private ones

resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.0.50"
  depends_on = [aws_internet_gateway.IGW]
  # the depends_on is to make sure that the IGW is created before the EIP
}

# 9. Create an Ubuntu server and install/enable apache2
  
resource  "aws_instance" "web-server-instance" {
  ami = "ami-0e35ddab05955cf57"
  instance_type = "t2.micro"    
  availability_zone = "ap-south-1a"
  key_name = "main-key"
  network_interface {
    // first one in a list
    device_index = 0
    network_interface_id = aws_network_interface.web-server-nic.id
  }
  // we will run all these commands in the user data, to install apache
  user_data = <<-EOF
                #!/bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
                sudo systemctl start apache2
                sudo bash -c 'echo your very first web server > /var/www/html/index.html'
                sudo bash -c 'echo hehe chubs'
                EOF
  tags = {
    Name = "web-server"
  }
}
```



Get the PPK file of your key pairs, go to putty an type ubuntu@3.x.x.x, whatever IP address is given.

Then go to PUTTY, SSH->Auth->Credentials->Private key file for authentication - enter `os@public IP` and this all will SSH u into the instance.


### **What is Inside the VPC?**

A **VPC (Virtual Private Cloud)** is your **isolated network** inside AWS. It contains:
1. **Subnets** → Smaller sections of the VPC for organizing resources (e.g., public/private).
2. **Network Interfaces (ENIs)** → Virtual network cards attached to EC2s for communication.
3. **EC2 Instances** → Virtual servers running inside subnets.
4. **Security Groups** → Firewalls controlling inbound/outbound traffic.
5. **Internet Gateway (IGW)** → Enables public internet access.
6. **Elastic IPs (EIPs)** → Static public IPs for external access.
7. **Route Tables** → Define how traffic flows inside/outside the VPC.
    
### **Why Do We Create a Network Interface (Step 7)?**

- By default, an **EC2 instance comes with an automatically assigned network interface** (NIC).
    
- However, in **Terraform**, we **explicitly create and attach a NIC** for **better control** over:
    - **Fixed private IP** within the subnet.
    - **Security group associations.**
    - **Ability to reassign the NIC to another instance** later if needed.

### **So Where is EC2?**

- **EC2 is inside the subnet**, which is inside the VPC.
- The **network interface (NIC) connects EC2 to the subnet and VPC.**
- The **Elastic IP (Step 8) gives the EC2 a public IP** so it can be accessed over the internet.

## So was EC2 inside subnet??
No,
- **By default**: If you create an EC2 **without specifying a network interface**, AWS **automatically assigns one** (with a private IP from the subnet).
    
- **In Step 7**: We **manually create and attach a network interface (ENI)** before launching the EC2.
    
- **In Step 9**: When the EC2 is created, it **uses the pre-created network interface** (instead of an auto-assigned one).

### 🔹 **What Actually Happens?**

1. **Step 7**: Creates a NIC **inside the subnet**, with a fixed private IP and security groups.
2. **Step 8**: Assigns an **Elastic IP** (public IP) to the NIC, so the instance can be accessed from the internet.
3. **Step 9**: Creates EC2 and attaches it to the **already existing NIC** (making its networking setup controlled manually).
    
### 🔹 **So, was the EC2 "outside" before?**

No, but before Step 9, **EC2 does not exist yet**—only the network is being prepared.  
When EC2 is created in Step 9, it is **inside the subnet from the beginning**, but instead of using AWS's auto-assigned networking, it uses the **custom network interface we made in Step 7**.
## Explanation of codes:
## **1. Create a VPC**

```js
resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}
```

- **VPC (Virtual Private Cloud)** acts as a logically isolated network within AWS.
- **CIDR block** defines the IP range (`10.0.0.0/16` means 65,536 IPs available).
- A **tag** is assigned to name the VPC (`production`).

---
## **2. Create an Internet Gateway (IGW)**

```js
resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.prod-vpc.id
}
```
- The **Internet Gateway (IGW)** allows instances inside the VPC to communicate with the internet.
- It is **attached** to the VPC (`prod-vpc`).

---

## **3. Create a Custom Route Table**

```js
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGW.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = aws_internet_gateway.IGW.id
  }
  
  tags = {
    Name = "Prod"
  }
}

```
- The **Route Table** defines how network traffic is directed inside the VPC.
- The first **route** (`0.0.0.0/0`) sends all IPv4 internet traffic to the **IGW**.
- The second **route** (`::/0`) is for **IPv6** and is linked to the **egress-only gateway**.
- A **tag** (`Prod`) is assigned.
    
---

## **4. Create a Subnet**

```js
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.prod-vpc.id
  cidr_block = "10.0.1.0/24"
  tags = {
    Name = "prod-subnet"
  }
}
```
- A **subnet** is created within the VPC, **allocating a smaller range (`/24`) of 256 IPs**.
- It allows instances to be placed in a **specific part of the VPC**.
    
---
## **5. Associate Subnet with Route Table**

```js
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}
```

- The **subnet** is linked to the **Route Table**, enabling **internet access** for resources inside the subnet.
    
---

## **6. Create a Security Group**

```js
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.prod-vpc.id
}
```
- A **Security Group** (SG) acts as a **firewall** to control inbound and outbound traffic.
- This SG is assigned to the **VPC** (`prod-vpc`).

### **Inbound Rules (Ingress)**
```js
  ingress {
    description      = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
```
- Allows:
    - **HTTPS traffic (443)** from anywhere (`0.0.0.0/0`).
    - **HTTP traffic (80)** from anywhere.
    - **SSH (22) access** from anywhere.

### **Outbound Rules (Egress)**

```js
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
```
- Allows **all outbound traffic** (`-1` means all protocols).
    
---

## **7. Create a Network Interface**

```js
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.0.50"]
  security_groups = [aws_security_group.allow_web.id]
}
```
- A **network interface** (`NIC`) is created in the **subnet**.
- It is assigned a **private IP** (`10.0.0.50`).
- The **Security Group (`allow_web`)** is attached to control traffic.

### **What Exactly Does Step 7 (Network Interface) Do?**

The `aws_network_interface` resource creates a **Virtual Network Interface (NIC)** inside the specified **subnet**.
#### **Why is this needed?**
- A **NIC** is a **bridge** between an EC2 instance and the VPC network.
- It allows the instance to communicate within the **private network (subnet)** and with the **public internet** when combined with an **Elastic IP** and **Internet Gateway**.
- It assigns a **fixed private IP (`10.0.0.50`)**, ensuring the instance always has the same internal address, which is useful for predictable networking.
- It attaches a **Security Group**, defining rules for inbound/outbound traffic.
    
---
## **8. Assign an Elastic IP (EIP)**

```js
resource "aws_eip" "one" {
  vpc                      = true
  network_interface        = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.0.50"
  depends_on               = [aws_internet_gateway.IGW]
}
```
- An **Elastic IP** is assigned to the **Network Interface** (`web-server-nic`).
- Ensures that the server has a **static public IP** for internet access.
- **Depends on IGW**, so EIP is created **after** the IGW.

### **Why Assign an Elastic IP (Step 8)?**

- Instances by default get a **dynamic public IP**, which changes if the instance stops/restarts.
- An **Elastic IP (EIP)** provides a **static public IP**, ensuring consistent access from the internet.
- This is necessary for **external services, remote SSH access, and hosting a public web server**.
- The **Internet Gateway (IGW)** is required to route internet traffic, so the `depends_on` ensures IGW is set up before assigning the EIP.
    
---
## **9. Create an Ubuntu Server and Install Apache**

```js
resource "aws_instance" "web-server-instance" {
  ami               = "ami-0e35ddab05955cf57"
  instance_type     = "t2.micro"
  availability_zone = "ap-south-1a"
  key_name          = "main-key"

```
- Creates an **EC2 instance** (Ubuntu) in the **ap-south-1a** availability zone.
- Uses a **specific AMI** for Ubuntu.
- Instance type is **`t2.micro`** (eligible for AWS Free Tier).
- The **SSH key pair** is `main-key` for login access.
    
### **Attach Network Interface**

```js
  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.web-server-nic.id
  }
```
- Assigns the **network interface (`web-server-nic`)** to this instance.
- **`device_index = 0`** ensures it is the **primary network interface**.

### **User Data (Apache Installation)**

```js
  user_data = <<-EOF
    #!/bin/bash
    sudo apt update -y
    sudo apt install apache2 -y
    sudo systemctl start apache2
    sudo bash -c 'echo your very first web server > /var/www/html/index.html'
    sudo bash -c 'echo hehe chubs'
  EOF
```
- Runs a **script** on startup:
    1. Updates system packages (`apt update`).
    2. Installs Apache (`apt install apache2`).
    3. Starts Apache (`systemctl start apache2`).
    4. Creates a **default index.html** (`your very first web server`).
    5. Prints `"hehe chubs"` (extra text, likely for debugging).
        
---

## **Final Summary**

- **Created a VPC** with a **subnet**.
- **Set up routing** via an **Internet Gateway** and **Route Table**.
- **Configured Security Groups** for **HTTP, HTTPS, and SSH**.
- **Created a network interface** with a **static private IP**.
- **Assigned an Elastic IP** for public access.
- **Launched an EC2 instance**, attached it to the network, and **installed Apache** automatically.
    

This setup results in a **publicly accessible** web server running Apache on Ubuntu.

