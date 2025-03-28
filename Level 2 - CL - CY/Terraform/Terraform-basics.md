Terraform is an Infrastructure as Code (IaC) tool that lets you define and manage cloud resources using configuration files. Instead of manually setting up servers, databases, and networking in a cloud provider like AWS, you write a Terraform script that specifies what resources you need.

When you run Terraform, it reads the configuration and creates or updates the infrastructure accordingly. It also tracks changes, so if you modify the config, Terraform will figure out what needs to be updated without rebuilding everything from scratch. This makes managing cloud infrastructure more **automated, consistent, and scalable**.

## Steps:
1.  Scope: Identify the infrastructure for your project.
2. Author: Write configuration to define your infrastructure.
3. Initialize: Install the required Terraform providers.
4. Plan: Preview the changes Terraform will make.
5. Apply: Make the changes to your infrastructure

# Terraform:
Written in HCL-Hashicorp Configuration Language. Install terraform from the website, and start working on it in VS code.

Go to AWS->profile->security credentials and generate credentials. You can use this in your terraform to connect to your AWS.

```js
  provider "aws" {
    region = "ap-south-1"
    access_key = "..."
    secret_key = "...."
}
```

Now, we go to the terraform documentation -> ec2 -> aws_instances
Here we can find examples on setting up am ec2 instance.

# Creating an EC2 instance:
Syntax:
```js
resource "<provider>_<resource_type>" "<resource_name>" {
    config options.....
     key = "value"
     key2 = "another value"
}
```

We did:
```js
  resource "aws_instance" "my-first-server" {
  ami           = "ami-0e35ddab05955cf57"
  instance_type = "t2.micro"
  tags = {
    Name = "My First Server"
  }
}
```

Now to run it on our AWS console, we go to or terminal.

- `terraform init` - this sees our codes and downloads the different plugins needed for that provider ( in our case AWS) and initiates a Terraform repo.
- `terraform plan` - gives an overview of what our code will do, what our code will do, create, destroy to see whatever happens.

- `terraform apply` - Will apply whatever we coded to our AWS.

```js

aws_instance.my-first-server: Creating...
aws_instance.my-first-server: Still creating... [10s elapsed]
aws_instance.my-first-server: Still creating... [20s elapsed]
aws_instance.my-first-server: Creation complete after 22s [id=i-09edbe7bd17c09d34]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Now we have completed creating an Ec2 instance.

If we do `terraform apply` again, it doesn't create another instance, it just deletes our old instance and create another instance, a new one, can be considered as updating.
Example - names can be updated. Terraform just updates the state of our current instance.

*Terraform is a declarative language*

## Destroy instances:
- `terraform destroy` - It will destroy the 1 EC2 instance that we have deployed from terraform.
Instead of this, we can even delete the defined resource code,  and when u do `terraform apply` i deleted the resource.


# Creating a VPC (Virtual Private Cloud)

### **What is a VPC in AWS?**

A **VPC (Virtual Private Cloud)** in AWS is like your own private section of the AWS cloud. It lets you create and control a network where your resources (like EC2 instances, databases, etc.) can securely communicate with each other and the internet.
### **Key Features of a VPC:**

1. **Isolation** – Your VPC is separate from others, meaning your resources won’t be exposed to external AWS users unless you allow it.
    
2. **Subnetting** – You can divide your VPC into smaller networks (subnets), typically for organizing resources into public and private sections.
    
3. **Security Controls** – You get **security groups** (firewall rules for instances) and **network ACLs** (rules at the subnet level).
    
4. **Internet & VPN Access** – You can connect your VPC to the internet using an **Internet Gateway (IGW)** or keep it private and link it to your on-premises network with a **VPN**.
    
5. **Peering & Transit Gateway** – You can connect multiple VPCs together for cross-network communication.
    

### **Basic VPC Structure:**
- **VPC** (overall network)
    - **Public Subnet** (accessible from the internet, usually for web servers)
    - **Private Subnet** (not directly accessible, used for databases, backend servers)
    - **Route Tables** (define traffic flow between subnets & internet)
    - **NAT Gateway** (lets private subnets access the internet without being exposed)
    - **Internet Gateway** (allows public subnets to connect to the internet)

### **Why Use a VPC?**
- To create **secure, customizable networks** for applications.
- To control **who can access** resources inside AWS.
- To **scale and isolate workloads** efficiently.

## Coding:

We can create a VPC code from tf and send to AWS.

## Creating a VPC:
```js
resource "aws_vpc" "first-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}
```

### Creating a subnet:
```js
resource "aws_subnet" "subnet-1" {
  // this ID references the above created VPC
  vpc_id     = aws_vpc.first-vpc.id
  cidr_block = "10.0.1.0/24"
  tags = {
    Name = "prod-subnet"
  }
}
```

In the VPC ID above, we reference the id property of the above created VPC - `first_vpc`