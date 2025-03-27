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

## Creating an instance:
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


## Destroy instances:
- `terraform destroy` - It will destroy the 1 EC2 instance that we have deployed from terraform.
Instead of this, we can even delete the defined resource code,  and when u do `terraform apply` i deleted the resource.
