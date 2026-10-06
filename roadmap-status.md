# 🗺️ Roadmap Status

## ✅ Completed through Day 36

### Week 1 — Networking
OSI, TCP/IP, IPv4/subnetting, ports.

### Week 2 — Network traffic
DNS, TCP/UDP, HTTP/HTTPS, TLS, browser-to-server flow.

### Week 3 — Linux
Filesystem, core commands, grep/find, permissions, users/groups, processes/services, sudo, pipes, redirection and command chaining.

### Week 4 — Integration
ping, traceroute, firewall/firewalld, `ss`, and network troubleshooting.

### Week 5 — Security fundamentals + SOC thinking
CIA, AAA, least privilege, defense in depth, threat/vulnerability/exploit/risk, IOC/TTP, phishing, brute force, password spraying, malware, credential theft, MITRE ATT&CK basics, and a mini SOC investigation.

## 🦈 Day 36 — Wireshark Basics

**Status: ✅ Completed**

### Practical work completed
- Started Wireshark
- Captured own traffic on `wlp0s20f3`
- Generated DNS, ping and HTTPS traffic
- Analyzed DNS request/response traffic
- Analyzed ICMPv6 Echo Request/Reply
- Analyzed TCP SYN
- Analyzed TCP SYN/ACK
- Analyzed final TCP ACK
- Observed TCP traffic carrying TLS
- Analyzed TLS Client Hello
- Observed TLS Application Data
- Practiced packet-level evidence-based analysis

## 🌐 Day 37 — Ethernet + IP Analysis

**Status: 🟡 In Progress**

### Studied so far
- Source MAC
- Destination MAC
- Ethernet II / EtherType
- Source IP
- Destination IP
- Protocol
- TCP source/destination ports
- TCP SYN flag
- Difference between frame length and TCP data length

### Example observed
An IPv6 TCP SYN packet:

```text
Source port: 48506
Destination port: 443
TCP flag: SYN
Frame length: 94 bytes
TCP data length: 0 bytes
```

### Still pending
The planned Day 37 IPv4 exercise using:

```bash
ping -c 5 1.1.1.1
```

followed by IPv4 analysis and the required SOC questions.

## 🎯 Next

Finish **Day 37 — IPv4 packet analysis**, then continue with Day 38 TCP + UDP packet analysis.

## 🧠 Current analyst mindset

```text
Evidence
   ↓
Observation
   ↓
Hypothesis
   ↓
More evidence
   ↓
Conclusion
```

> Keep the repository evidence-based: document what was actually learned, practiced and investigated.
