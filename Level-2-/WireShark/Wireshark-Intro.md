# What is it?
Wireshark is a **network protocol analyzer** used for capturing, inspecting, and analyzing network traffic in real-time. It allows users to see what's happening at a deep level in a network, making it useful for troubleshooting, security analysis, and network optimization.

### **Key Features of Wireshark:**
- **Packet Capture** – Captures live network traffic or analyzes previously saved packet data.
- **Protocol Analysis** – Supports a vast range of network protocols (TCP, UDP, HTTP, DNS, etc.).
- **Filtering & Searching** – Apply powerful display filters to focus on specific traffic.
- **Decryption** – Can decrypt certain encrypted protocols (like SSL/TLS) if keys are available.
- **Graphical & Statistical Tools** – Visualize traffic patterns and trends.
- **Cross-Platform** – Available for Windows, macOS, and Linux.
    

### **Common Use Cases:**
- **Network troubleshooting** – Identify latency, packet loss, or misconfigured devices.
- **Security analysis** – Detect suspicious traffic or potential attacks.
- **Learning networking concepts** – Understand how network protocols work in detail.

---

![[Pasted image 20250328133722.png]]

Every row we see is a packet sent.

1 session of packets identification is called Pcap (Packet Capture)

![[Pasted image 20250328134322.png]]

I am 192.168.1.4, we can see communication with other IP addresses.
You can right click on any IP and apply filters so that only 1 set of information is visible at once.

### **TLS + HTTP = HTTPS**
## TLS and SSL:

TLS (**Transport Layer Security**) and SSL (**Secure Sockets Layer**) are cryptographic protocols that secure data transmission over networks, such as HTTPS websites, email, and messaging apps. SSL (developed in the 1990s) had vulnerabilities, so TLS replaced it, with **TLS 1.2 and TLS 1.3** being the most secure versions today. TLS encrypts data between clients (browsers) and servers, preventing hackers from intercepting sensitive information like passwords or credit card details. Modern systems use **TLS instead of SSL**, but people still refer to it as "SSL" out of habit.

TLS encryption in **browser-to-server (HTTPS) communication** uses **both asymmetric and symmetric encryption**:

1️⃣ **Asymmetric Encryption (Public/Private Key)**
- Used **only during the TLS handshake** to securely exchange a **shared session key**.
- The browser encrypts the session key using the server’s **public key** (from its SSL certificate).

2️⃣ **Symmetric Encryption (Session Key)**
- After the handshake, **all data (HTML, CSS, API calls, etc.) is encrypted using symmetric encryption** (AES, ChaCha20, etc.).
- This ensures **fast** and **secure** communication.

So, TLS **starts with asymmetric encryption** (for key exchange) and then switches to **symmetric encryption** (for data transfer)

## Stuff i learnt:
1. Adding filters to view 1 protocols connections, and analyzing them.
2. Adding buttons for filters.
3. Looking at conversations to go in depth into communications. 


## Coloring rules:
go to view->coloring rules, to see them.

# Conclusion:

1. When viewing http transmissions, i could view the HTML page in wireshark, indicating its unencrypted nature, whereas in TLS, the data was encrypted. ![[Pasted image 20250328140216.png]]
The hexadecimal data on the right is actual data, encrypted in TLS and unencrypted in HTTPs case.

This is how phishing works, a phisher can get your credentials in this format, if you enter your credentials in an HTTP unsecure website. So never enter credentials on an HTTP website.



## Delta time:
I added delta time, in preferences->columns->add delta time
**Delta Time** in Wireshark is the time difference between packets.
- **"Time delta from previous captured frame"** shows the gap between the current and last captured packet.
- **"Time delta from previous displayed frame"** shows the gap between displayed packets (after applying filters).

**Delta Time is useful for:**
1️⃣ **Detecting Network Delays & Performance Issues** 🚀
- High delta times between packets may indicate **latency**, **packet loss**, or **network congestion**.

2️⃣ **Analyzing Attack Patterns & Anomalies** 🔍
- Unusual delays or **sudden spikes in delta time** can signal **DoS attacks**, **slowloris attacks**, or irregular traffic patterns.



# For MARVEL TASK OUTCOMES:

- Diagnose problems like latency, packet loss, or retransmissions.
- Look for packets marked with issues (e.g., retransmissions or duplicate acknowledgments).
- Use tools like the "Statistics" menu to view summaries and graphs.

### **1️. Identify Packet Issues**

#### **A. Looking for Retransmissions & Packet Loss**
- `tcp.analysis.retransmission` → Shows retransmitted packets (indicates packet loss).
- `tcp.analysis.duplicate_ack` → Detects duplicate ACKs (possible lost packets).
- `tcp.analysis.lost_segment` → Shows lost TCP segments.
        
- **How to Interpret?**
    - **Many retransmissions** → Network congestion or packet loss.
    - **Duplicate ACKs** → Possible packet loss or reordering.
    
![[Pasted image 20250328145015.png]]

In statistics, TCP stream graphs, checking Round Trip Latency(RTT) can help us test our Network Communication Efficiency. In networking, Round Trip Time (RTT) measures the time it takes for a data packet to travel from a source to a destination and back, serving as a key indicator of network latency and connection quality, typically measured in milliseconds.

If your **RTT graph in Wireshark is an upside-down linear trend** (decreasing over time), it means:

✅ **Improving Network Performance** – Packets are reaching their destination and returning **faster over time**.  
✅ **Reduced Congestion** – Possible **network optimization, better routing, or congestion clearing up**.  
✅ **TCP Slow Start Ending** – If the connection initially had high RTT but stabilized, this could be due to **TCP congestion control mechanisms** adjusting.


C. IO graphs for traffic analysis
![[Pasted image 20250328145801.png]]
By applying the filter **`tcp.analysis.retransmission`** in **Statistics > IO Graphs**, you can visualize how often packets are being retransmitted over time. A **high frequency of retransmissions** indicates **packet loss**, which can be caused by network congestion, unstable connections, or poor signal quality (especially in Wi-Fi networks). If the retransmissions appear in **bursts**, it might suggest temporary network instability, while a **steady increase** over time could indicate a persistent issue. This analysis helps in diagnosing potential **network bottlenecks**, **performance degradation**, or even possible **cyberattacks** (e.g., DoS attempts). 


--- 

# Advanced filters:

1. `!(arp or stp or lldp or cdp)` , we can include whatever we want in here to hide protocols.

2. `tcp.flags.syn==1`, finding SYN flag (first step) of 3 way handshake.

When i ran this, i got 30/1017 packets visible, indicating it.
### SYN Packet Detection 🚀
This filter in Wireshark **captures only TCP packets with the SYN flag set**.
#####  What Does It Mean?
- The **SYN (synchronize) flag** is used in the **TCP handshake** to **initiate a connection**.
- A packet with `tcp.flags.syn == 1` means **a client is requesting to start a new TCP connection** with a server.

The 3 way handshake consists of SYN, SYN-ACK and ACK.
##### **What Can We Conclude?**
1️⃣ **Normal Behavior:** If you see a SYN followed by **SYN-ACK** and **ACK**, it's a valid **TCP 3-way handshake** (connection established).  
2️⃣ **Port Scanning:** Many SYN packets **without SYN-ACK responses** may indicate a **port scan** (e.g., from Nmap).  
3️⃣ **SYN Flood Attack:** A **large number of SYN packets without ACKs** can mean a **SYN flood attack** (DoS attack trying to overwhelm the server).

This task helped me conclude my understandings of Computer Networking.




3. `tcp.analysis.flags`
![[Pasted image 20250328144229.png]]
Wireshark **flags packets** based on unusual behavior, errors, or specific protocol conditions. Some common flagged packets include:
### **TCP Flags**
Wireshark highlights TCP packets based on their **flags**:
- **SYN** → Connection initiation (`tcp.flags.syn == 1`)
- **RST** → Connection reset (`tcp.flags.reset == 1`)
- **ACK** → Acknowledgment (`tcp.flags.ack == 1`)
- **URG** → Urgent data (`tcp.flags.urg == 1`)
    
### **Wireshark-Specific Packet Warnings**
Wireshark automatically flags:
- **Retransmissions** → Packets resent due to lost data (`tcp.analysis.retransmission`)
- **Out-of-Order Packets** → Packets arriving out of sequence (`tcp.analysis.out_of_order`)
- **Duplicate ACKs** → Possible sign of packet loss (`tcp.analysis.duplicate_ack`)
- **Zero Window** → Receiver's buffer is full (`tcp.analysis.zero_window`)
    
### **Protocol-Specific Warnings**
- **Malformed Packets** → Corrupted or incorrect formatting (`frame.len` mismatch, invalid checksums).
- **TLS Alerts** → Errors in TLS handshake (e.g., invalid certificates).
- **ICMP Errors** → Network unreachable, time exceeded, etc.


3. `tcp.flags.reset==1`
### **`tcp.flags.reset == 1`** → **TCP RST (Reset) Packets** 
This filter captures **TCP packets with the RST (Reset) flag set**, meaning the connection is being **forcibly closed**.

### **🔍 What Does It Mean?**
- A **TCP RST** packet is sent when a device **rejects or abruptly terminates** a connection.
- Unlike a **graceful FIN-ACK termination**, an RST **immediately kills the connection**.
    
### **What Can We Conclude?**

1️⃣ **Normal Behavior:**
- A **server rejects a request** to a closed or blocked port.
- A **client quickly closes a bad connection** (e.g., app crash).

2️⃣ **Error Conditions:**
- **Mismatched sequence numbers** → Connection out of sync.
- **Firewall blocking traffic** → Firewalls may send RST packets when blocking unwanted connections.

3️⃣ **Possible Attacks:**
- **RST Flood Attack** → Multiple RST packets can **disrupt TCP connections** (used in DoS attacks).
- **Session Hijacking Attempt** → Attackers forge RST packets to kill active connections.






-- Check out `malware-traffic-analysis.net` to get pcap files for analysis.