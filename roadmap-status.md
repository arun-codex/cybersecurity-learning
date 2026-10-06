# 🗺️ Roadmap Status

## ✅ Completed through Day 37

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

## 🌐 Day 37 — Ethernet + IP Analysis

**Status: ✅ Completed**

### Completed
- Source MAC
- Destination MAC
- EtherType
- IPv4 source/destination
- IPv4 TTL
- Protocol
- IPv4 total length
- ICMP Echo Request
- ICMP Echo Reply
- Packet request/reply comparison
- SOC questions using packet evidence

### Observed IPv4 ICMP exchange

```text
192.168.1.9  →  1.1.1.1
ICMP Echo Request

1.1.1.1  →  192.168.1.9
ICMP Echo Reply
```

Request:
- TTL 64
- ICMP Type 8
- Total Length 84 bytes

Reply:
- TTL 58
- ICMP Type 0
- Total Length 84 bytes
- Selected response time ~42 ms
- Sequence 5

### Analyst lesson
Use packet evidence to answer:
who initiated, what protocol was used, whether a response occurred, how often it occurred, and what evidence supports the conclusion.

## 🎯 Next

**Day 38 — TCP + UDP Packet Analysis**

Focus:
- SYN, ACK, FIN, RST, PSH
- TCP handshake
- TCP data
- TCP termination
- Client/server ports
- UDP DNS query
- TCP vs UDP

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
