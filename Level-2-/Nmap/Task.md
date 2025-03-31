

#### Conclusions from my network scan:

My network had 6 devices connected to it, which were responsive when a ran an `agressive scan`. I recorded the observations and concluded that:
1. In a SYN scan, some devices had firewall enables, and Nmap was not able to bypass that to get the required information.
2. My router had some services running like Telnet, DNS, HTTPS. Telnet would mean my router is outdated, and is a potential vulnerability.
3. It also had an expired SSL certificate (2009) which might make it vulnerable to brute force attacks.
