# What is it?
SSH is a software package that enables secure system administration and file transfers over insecure networks. It is used in nearly every data center and in every large enterprise.

## The SSH protocol
The SSH protocol uses encryption to secure the connection between a client and a server. All user authentication, commands, output, and file transfers are encrypted to protect against attacks in the network. For details of how the SSH protocol works, see the [protocol page](https://www.ssh.com/ssh/protocol/). To understand the SSH File Transfer Protocol, see the [SFTP](https://www.ssh.com/ssh/sftp) page.

The protocol works in the client-server model, which means that the connection is established by the SSH client connecting to the SSH server. The SSH client drives the connection setup process and uses public key cryptography to verify the identity of the SSH server. After the setup phase the SSH protocol uses strong symmetric encryption and hashing algorithms to ensure the privacy and integrity of the data that is exchanged between the client and server.

![umm](https://www.ssh.com/hs-fs/hubfs/SSH_Client_Server.png?width=834&name=SSH_Client_Server.png)

## SSH provides strong encryption and integrity protection

Once a connection has been established between the SSH client and server, the data that is transmitted is encrypted according to the parameters negotiated in the setup. During the negotiation the client and server agree on the symmetric encryption algorithm to be used and generate the encryption key that will be used. The traffic between the communicating parties is protected with industry standard strong encryption algorithms (such as AES (Advanced Encryption Standard)), and the SSH protocol also includes a mechanism that ensures the integrity of the transmitted data by using standard hash algorithms (such as SHA-2 (Standard Hashing Algorithm)).

### **Public Keys and Keys in SSH**

SSH (Secure Shell) uses **public-key cryptography** for secure authentication and communication. Let's break it down:

1. **Public and Private Keys (Asymmetric Cryptography)**
    - **Private Key** (`id_rsa` or `id_ecdsa`, etc.): A secret key that is kept secure on your local machine.
    - **Public Key** (`id_rsa.pub`, `id_ecdsa.pub`, etc.): A key derived from the private key and shared with remote servers.
        
    
    These two keys work together:
    - The public key is **stored on the server** in `~/.ssh/authorized_keys`.
    - The private key is **kept on your local machine**.
    - When you try to SSH into the server, the server verifies that you own the private key without actually seeing it.
        
2. **Session Keys (Symmetric Cryptography)**
    - After authentication, SSH **switches to symmetric encryption** using a **session key** for encrypting the actual communication.
    - The session key is **randomly generated** for each connection and is **securely exchanged** using the public-private key pair.

### **Encryption in SSH**

1. **Authentication (Public-Key Cryptography)**
    - Your private key **never leaves your machine**.
    - Instead, SSH uses **challenge-response authentication** to verify you own the private key.
    - If password authentication is used instead of SSH keys, the password is **encrypted** before transmission.
        
2. **Data Transmission (Symmetric Encryption)**
    - Once authenticated, SSH encrypts all communication between client and server.
    - **Commands, file transfers, and shell interactions** are all encrypted.
    - The encryption uses **symmetric ciphers** (e.g., AES, ChaCha20) for performance.

## What is SSH keys?
private key - super secret, 
public key - public

To access a server, what we do is:
1. Generate `private key` from our laptop, and we send our public key to the server. And we say to SSH, we need to connect to that server and use the private key.

2. Server encrypts stuff using public key, and sends it to our laptop, where we will decrypt it using our `private key`,  n sends it back too the server, and now, server can verify if we are who we truly are, and an SSH connection is formed.

### **How SSH Keys Work** (Simplified)
1️⃣ You generate an **SSH key pair** (🔑):
- **Private Key** (Super Secret, stays on your machine).
- **Public Key** (Safe to share, sent to the server).

2️⃣ The **server stores your public key** in `~/.ssh/authorized_keys`.

3️⃣ When you try to **SSH into the server**, the process goes like this:
- Server **encrypts a challenge** using your **public key**.
- Your laptop **decrypts it** using the **private key** and responds.
- Server checks if the response is valid → ✅ **Access Granted! SSH connection done.
### What Happens Next?**

✅ **1. Session Encryption Setup** – SSH negotiates a **symmetric encryption key** (AES, ChaCha20, etc.) to secure all further communication.  
✅ **2. Secure Data Exchange** – Now, every command you type and every response from the server is **encrypted** using this session key.  
✅ **3. You Get a Remote Shell** – You can now run commands, transfer files (`scp`, `rsync`), or even tunnel traffic securely.

Basically, SSH first **verifies you** (authentication) → then **secures the session** → and **finally lets you interact** with the remote server. 


## Basically, 
**SSH uses asymmetric encryption for authentication** and then switches to **symmetric encryption for secure communication**.

### **Breaking it Down:**
1️⃣ **Asymmetric Encryption (RSA, ECDSA, Ed25519, etc.)**
- Used **only during authentication** (public-private key exchange).
- Ensures that only the **right person** can access the server.
    
2️⃣ **Symmetric Encryption (AES, ChaCha20, etc.)**
- Once authenticated, SSH generates a **session key** using key exchange (Diffie-Hellman, etc.).
- Both client & server use this key for **fast, secure communication**.

🔹 **Why switch to symmetric encryption?**
- Asymmetric encryption is **slow**, so SSH only uses it for **authenticating**.
- Symmetric encryption is **faster**, so it's used for the **actual data transfer**.
    

That’s SSH in a nutshell—**asymmetric to get in, symmetric to stay secure**! 




## TASK 3: SSH

Secure Shell (SSH) is a network communication protocol that enables two computers to communicate.

**Task Outcome**: Write a script to SSH into a server, search the entire server for public/private keys, and upload them to another server.

### **SSH Keys & Encryption - Summary**

#### **1. SSH Key Pairs (Asymmetric Cryptography)**
- SSH uses a **public-private key pair** for authentication.
- **Private Key (`id_rsa`)** → Kept secret on the client.
- **Public Key (`id_rsa.pub`)** → Stored on the server (`~/.ssh/authorized_keys`).
- Authentication works by proving the client has the **private key** without revealing it.
    

#### **2. How SSH Authentication Works**
1. The server sends a **random challenge** to the client.
2. The client **encrypts it using its private key**.
3. The server **decrypts it using the client’s public key** (from `authorized_keys`).
4. If it matches, access is granted.

#### **3. What is Encrypted in SSH?**
- **Authentication Process** (Asymmetric encryption).
- **Data Transmission** (Symmetric encryption using a session key).
- **Integrity Verification** (MAC - Message Authentication Code).
    

#### **4. Finding SSH Keys on a Server**
- SSH keys **should** stay on the client, but they **can be found** on a server due to:
    - **Accidental uploads** by users.
    - **Stored in backups** or misconfigured permissions.
    - **Hardcoded in scripts** or inside **Docker/VM images**.
        

#### **5. Searching for SSH Keys on a Server**
- Common locations:
    - **User-specific:** `~/.ssh/` (id_rsa, id_rsa.pub, authorized_keys).
    - **System-wide:** `/etc/ssh/` (host keys).
    - **Backups & scripts:** `/home/user/backup/`, `/var/backups/`.

    

#### **6. What Can Be Done After Finding SSH Keys?**
- **For Security Auditing:**
    - Check if private keys are **unprotected or misplaced**.
    - Ensure they are **properly secured with permissions** (`chmod 600`).
    - Report & remove unnecessary keys.
- **For Malicious Use (Ethical Warning 🚨):**
    
    - Stolen private keys can allow unauthorized access to other servers.



