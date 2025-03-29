To search the server for private and public keys, i used

```bash
find / -type f -name "*.pub" 2>/dev/null
```

The command `find / -type f -name "*.pub" 2>/dev/null` searches for all regular files (`-type f`) with a `.pub` extension (typically public keys) across the entire filesystem (`/`). The `2>/dev/null` part suppresses error messages (like "Permission denied") by redirecting them (`2>`) to `/dev/null`, a special device that discards data. This ensures the output only shows found files without cluttering the terminal with errors.



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