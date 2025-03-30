
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
    // this means all traffic will be sent to this IGW
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGW.id
  }

  tags = {
    Name = "Prod"
  }
}

# 4. Create a Subnet
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.prod-vpc.id
  cidr_block = "10.0.1.0/24"  //the subnet we will use

  tags = {
    Name = "prod-subnet"
  }
}

# 5. Associate subnet with Route Table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}


# 6. Create Security Group to allow port 22, 80, 443
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.prod-vpc.id


  //defining ports routes
  
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
  
    egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"  //this means any protocol
    cidr_blocks      = ["0.0.0.0/0"]
  }
  tags = {
      Name = "allow_web"
  }
}



# 7. Create a network interface with an IP in the subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]  // any one within the subnet
  security_groups = [aws_security_group.allow_web.id]
  # the above line is to assign the private security group to the network interface  
}

# 8. Assign an elastic IP to the network interface crearted in step 7
# now we will assign private ones

resource "aws_eip" "one" {
 // vpc                       = true
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.IGW]
  # the depends_on is to make sure that the IGW is created before the EIP
}

# 9. Create an Ubuntu server and install/enable apache2 

resource  "aws_instance" "web-server-instance" {
  ami = "ami-01938df366ac2d954"
  instance_type = "t2.micro"    
  availability_zone = "ap-southeast-1a"
  key_name = "umm"
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

