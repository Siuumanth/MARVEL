<br>
# Sumanth - Level 2 Task Report

## Task 1: Linux Based Task with Socket.io

Learnt about Web Sockets, how they work and why they are so efficient and widely used in place of the normal request response cycle for real time  applications. I also built a real time chat application using Node js, socket.io module that uses HTML for frontend, Express js for the APIs and learnt how to identify and debug errors from the inspect tab in browsers.

### Why Web Sockets?
In a normal client server application , the service request can only be initiated by the client, and a response is sent back by the server. This means the server cannot send a response without a request. In real time chat applications, or news apps , we see ourselves getting real time updates and messages sent by the corresponding server. 

One method used to solve this is through `polling`, where we repeatedly send requests to the server to check for updates. This is inefficient, as most of the times , the responses are empty and the server load increases as well. This is why we use web sockets.

Web sockets are a communication protocol. used to connect the client and server to allow for bidirectional communication, by which the client and the server can communicate seamlessly. The normal HTTP request sent by the client is upgraded to a web socket connection on the clients request. 

This program sets up an Express server and integrates Socket.IO for real-time communication, allowing clients to send messages that the server then broadcasts to all connected users. It listens for client connections, handles messages, and serves an HTML page for the frontend.

[Github Link](https://github.com/Siuumanth/MARVEL-/tree/main/Codes/socket)


![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/1-code.png?raw=true)

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/1-website.png?raw=true)




<br>
## Task 2: Git Bash and GitHub

I learnt about the different Git processes like committing, push, pull, cloning, forking, branching, merging. I then learnt the different git commands, and how to use Git Bash, to navigate, add files and commit changes and initiate a pull request to the repository. I then learnt the concepts of branching and merging, their importance and how to implement it.

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/2-main.png?raw=true)

### Branching and Merging :
Branching allows you to create a separate version of the code, and work on new features or fixes, without affecting the main project. When the feature is ready, the changes can be merged with the main branch.

Suppose you are working in a team to build a website , and you are tasked with working on a feature. To work on it efficiently, you need to create a branch, to work on that feature, which is basically a copy of the main project. Your work on this branch will not affect the main branch, thus allowing you to test and work on the feature. After its done, you will merge your feature branch to the main branch, thus successfully adding the feature.

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/2-merging.png?raw=true)


#### Merge conflicts:
A **merge conflict** occurs in Git when two branches have changes to the same part of a file, and Git cannot automatically decide which changes to keep. This often happens when multiple people edit the same lines of a file or make incompatible changes. To solve this, Git will need you to manually resolve this conflict, i.e. choose the correct branch you want to merge, or you can even manually add changes.

<br>
## Task 3: OSI MODEL

I learnt how the internet works, how every communication process related to it is streamlined by the different layers of OSI Model, TCP/IP model protocols and methods. I completed a 4 hour course that explained how the internet works, how IP addressing and the different protocols work. 

In short, when a webpage is requested by the client :

- The HTTP request is directed from the ISP/Router of the client to the particular server that is resolved by Domain Name System( DNS ). The DNS identifies the IP address of the nearest server by the domain name.

- The specific server receives the request, and give the response corresponding to it, and the information like HTML files , json , etc. are sent through the same route to the client.

The communication is streamlined the various protocols that are grouped conceptually in different layers. In each layer, the data is passed down in different formats. The layers are :

1. `Application layer `: These are your software applications like browsers.
2. `Presentation layer` : Data from AL will be encrypted, translated, abstracted, compressed and sent to the next layer.
3. `Session layer` : Helps in setting up and managing connections, authorization and authentication.
4. `Transport layer` : Data is segmented and every segment contains source and destination ports and sequence numbers. It manages error control, flow control by TCP and UDP.

5. `Network layer` : Internet Protocol (IP) is a key protocol at this layer, responsible for assigning unique IP addresses to devices and facilitating communication between different networks. The router or your ISP lies here.

6. `Datalink layer` : Receives data packets from the NL. Data is framed and unframed here, header, payload is added, and at the receiver's side, MAC addresses is added to them which allows direct communication with the host and the network.

7. `Physical layer` : It receives the data and is responsible for transmitting raw binary data over a physical medium such as cables, radio waves or fiber optics.
<br>

![OSI model](https://github.com/Siuumanth/MARVEL/blob/main/Images/3-osi.png?raw=true)



<br>

## Task 4: Encryption Techniques
I learnt about encryption, what it is, the terms related to it like key, cipher, ciphertext, etc., and its importance in our daily life to secure our data.
I then learnt about some common effective techniques of encryption and implemented them using the pycryptodome library in python. Some encryption techniques I implemented are:

1.  `Advanced Encryption Standard ( AES )` : AES is a type of symmetric encryption that works by breaking the plain text (your original message) into fixed-size blocks (usually 16 bytes) and applying multiple rounds of transformations using a secret key. The ciphertext can be decrypted using the same key.

![AES](https://github.com/Siuumanth/MARVEL/blob/main/Images/4-AES.png?raw=true)

2. `Asymmetric encryption, or RSA` : also known as public-key cryptography, involves the use of two distinct but mathematically related keys: a public key and a private key. This process is slower than AES as it uses different keys for both encryption and decryption, but it provides high security and remains one of the best techniques.

![rsa](https://github.com/Siuumanth/MARVEL/blob/main/Images/4-RSA.png?raw=true)

3. `PBKDF2 (Password-Based Key Derivation Function` :is a cryptographic function used to derive a strong encryption key from a weak password. The process involves:

- A random value (salt) is added to the password to ensure that even identical passwords generate different keys. Iterations: The hashing process is repeated many times, making brute-force attacks more difficult by increasing computational cost. 
- Hashing uses a cryptographic hash function, which is one-way and irreversible, making it impossible to reverse engineer the password from the derived key. 

- We see its use case in our daily life when we try to login with our password.

![alt](https://github.com/Siuumanth/MARVEL/blob/main/Images/4-PK.png?raw=true)


4. `Cipher Block Chaining( CBC )` : is a mode of encryption used with block ciphers. 

 - Data is divided into blocks. and the first block is combined with a random piece of text called the Initialization Vector( IV ). After combining, its encrypted using a cipher likes AES.
 - For the next block, the previous encrypted block is combined with the new plaintext block before encrypting.  This "chains" the blocks together.
 - `Chaining :` Each block depends on the previous one, making it harder to tamper with individual blocks.


![alt](https://github.com/Siuumanth/MARVEL/blob/main/Images/4-CBC.png?raw=true)
[Link to the colab file](https://colab.research.google.com/drive/1HpsAe0URFra_V3qzI_l5_c2qTdaRETd2?usp=sharing)


<br>

## Task 5: IP Addressing and Protocols

#### IP Addressing:
Each device that uses a network receives an IP address and a special identifier number. IP Addresses are necessary for routing data packets between devices and enabling Internet communication between devices. 
#### Subnetting
A network is divided into smaller subnetworks, or subnetworks, through the process known as a subnetting . For this purpose, a network part of the IP address is created by taking bits from the host part. The host party identifies the specific device on the subnetwork, while the network party identifies the subnetwork as a whole.

#### Webscraping :
Web scraping is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format, which can be parsed to obtain information.

I first learnt how about the `robots.txt` file , which are txt files embedded in websites that contain  instructions for bots that tell them which webpages they can and cannot access. 

Then, using Beautiful Soup, I learnt:
- how to get HTML pages from URLs
- different methods used to parse the HTML files 
- how we can look for any particular data within HTML files
- Using regex, extracting `IP addresses` from the webpages


![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/5-BS.png?raw=true)


![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/5-IP.png?raw=true)

##### But whose IP addresses are those ?
Some addresses are the IP addresses of the servers hosting the website we're scraping from. Some are part of the public network, and some are part of another private network.

When scraping websites, we're usually connecting to a public IP address that belongs to a server, and that server is part of a larger network. Subnetting helps the network divide and allocate resources efficiently across different segments.

[Link to the colab file](https://colab.research.google.com/drive/1wfzUOkgFx6zPCAJ1MqeZoB5Q7iJqp5U2?usp=sharing)

<br>

## Task 6: Kali Linux and SSH

I first installed and set up Kali Linux through Virtual Box. I began my journey into penetration testing by first learning how the internet works, and how private and public IP addressing works through NAT( Network Addressing Protocol ) . I then learnt all the basic linux commands for navigation, and the different networking commands like `ifconfig, netdiscover,etc.` 

I then moved on to learning Penetration Testing, I got an overview of how attacks take place, basically it starts by scanning networks, finding vulnerabilities or loop holes and getting versions of the different services through tools and finally exploiting the version specific vulnerabilities.

### Nmap :
I then started learning about network exploration through `Nmap`. It is a powerful network discovery tool that can be used for :
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


I also learnt what is `Secure Shell Protocol ( SSH )` , how it works and how it can be used for exploitation, even played a couple of [Wargames by OverTheWire](https://overthewire.org/wargames/bandit/), where I SSHed into their server and solve puzzles using different linux commands.

<br>

## Task 7: Databases

I started by first learning about how mysql works, and the different commands in it which are classified into Data Definition Language( DDL ) and Data Manipulation Language ( DML ).
I learnt how to create data and insert it into the database, updating, deleting and getting data from the tables. These operations are collectively known as CRUD operations ( Create Read Update and Delete ).

By using `mysql` with a programming language for handling the logic ( backend ), we can simplify and streamline these CRUD operations for any use case. Combining with backend technologies like Flask, Django , or Nodejs and Expressjs , we can create suitable APIs to handle communication with the database.

I first used `Flask`, along with an `ORM - SQL Alchemy` to create a crud backend with SQLite database, and defined APIs to communicate with the database table, which worked pretty well.
The HTTP methods for CRUD are namely :
- POST
- GET
- PUT
- DELETE

I then thought of exploring different technologies and learnt how to build the same CRUD backend with `Nodejs` and `Expressjs` without an ORM. I used `mysql` module to create a database and created APIs with Express to handle different type of requests for CRUD. I then tested the APIs in Postman - a tool used to test your APIs and backend without a frontend.

[Github link](https://github.com/Siuumanth/MARVEL-/tree/main/Codes/Database)

![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/7-code.png?raw=true)


![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/7-GET.png?raw=true)


![alt](https://github.com/Siuumanth/MARVEL-/blob/main/Images/7-PUT.png?raw=true)