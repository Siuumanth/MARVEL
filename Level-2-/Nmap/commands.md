### **Nmap Cheat Sheet – Main Commands and Flags** 🚀

#### **1️⃣ Basic Scans**

| Command                   | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `nmap <target>`           | Basic scan (default: TCP SYN scan on top 1000 ports).   |
| `nmap -p <port> <target>` | Scan a specific port. Example: `nmap -p 22 192.168.1.1` |
| `nmap -p- <target>`       | Scan **all 65535** ports.                               |
| `nmap -sP <target>`       | Ping scan (check if host is up).                        |
| `nmap -sn <target>`       | No port scan, only host discovery.                      |

---

#### **2️⃣ Port Scanning Techniques**

|Flag|Description|
|---|---|
|`-sS`|**Stealthy SYN scan** (most common, requires sudo).|
|`-sT`|**TCP Connect scan** (used if no root privileges).|
|`-sU`|**UDP scan** (for UDP services like DNS, SNMP).|
|`-sA`|**ACK scan** (used to check firewall rules).|
|`-sF`|**FIN scan** (bypasses some firewalls).|
|`-sN`|**Null scan** (no flags set, used for stealth).|
|`-sX`|**Xmas scan** (sets FIN, PSH, URG flags).|

---

#### **3️⃣ Service & Version Detection**

|Flag|Description|
|---|---|
|`-sV`|Detect service versions (e.g., Apache, OpenSSH, MySQL).|
|`-A`|**Aggressive scan** (OS detection, version detection, script scanning, traceroute).|
|`--version-intensity <level>`|Adjust service detection (0-9, higher = more aggressive).|

---

#### **4️⃣ OS & Host Detection**

|Flag|Description|
|---|---|
|`-O`|Detect OS (needs root privileges).|
|`--osscan-guess`|Guess OS if detection is uncertain.|
|`-sL`|List targets without scanning (DNS resolution only).|

---

#### **5️⃣ Scan Output & Logging**

|Flag|Description|
|---|---|
|`-oN <file>`|Save output in normal text format.|
|`-oX <file>`|Save output in XML format.|
|`-oG <file>`|Save output in grepable format.|
|`-oA <basename>`|Save in **all formats** (normal, XML, grepable).|

---

#### **6️⃣ Firewall/IDS Evasion**

|Flag|Description|
|---|---|
|`-D <decoy1,decoy2>`|Use decoy IPs to confuse IDS.|
|`-S <spoofed_ip>`|Spoof source IP address.|
|`-f`|Fragment packets (bypass firewalls).|
|`--mtu <size>`|Change packet size (evasion technique).|
|`--scan-delay <time>`|Add delay between packets (bypass rate-limiting).|

---

#### **7️⃣ Network Scanning**

|Command|Description|
|---|---|
|`nmap 192.168.1.0/24`|Scan all devices in a subnet.|
|`nmap -sn 192.168.1.0/24`|List active hosts without port scanning.|
|`nmap --traceroute <target>`|Perform traceroute to a target.|

---

#### **8️⃣ Advanced Techniques**

|Flag|Description|
|---|---|
|`--script=<script>`|Run a specific NSE (Nmap Scripting Engine) script.|
|`--script=vuln`|Scan for known vulnerabilities.|
|`-Pn`|**Disable host discovery** (treat all hosts as online).|
|`-T<0-5>`|Set scan speed (0 = slowest, 5 = fastest).|

---
### **Ping Scan (`-sn`) vs No Ping Scan (`-Pn`) in Nmap**

|Feature|**Ping Scan (`-sn`)**|**No Ping Scan (`-Pn`)**|
|---|---|---|
|**Purpose**|Checks if hosts are up|Assumes all hosts are up|
|**How It Works**|Uses ICMP Echo Request (ping) + TCP SYN/ACK|Skips host discovery, directly scans ports|
|**When to Use?**|When you want to discover live hosts before scanning|When ping is blocked (firewall, IDS/IPS)|
|**Speed**|Faster|Slower (scans every IP)|
