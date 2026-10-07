# 🗺️ Roadmap Status

## ✅ Completed through Day 38

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

## 🔵 Day 38 — TCP + UDP Packet Analysis

**Status: ✅ Completed**

### TCP completed
- TCP SYN
- TCP SYN/ACK
- TCP ACK
- Three-way handshake
- TCP data
- PSH + ACK
- TCP FIN + ACK termination
- Client/server port analysis
- TCP payload length analysis

### UDP/DNS completed
- UDP DNS query
- UDP source/destination ports
- DNS query for `example.com`
- DNS response
- Transaction ID `0x39df`
- Two A records:
  - `104.20.23.154`
  - `172.66.147.243`
- Response time ~65.8 ms
- No TCP-style handshake for this DNS exchange

### Core lesson
```text
TCP:
SYN → SYN/ACK → ACK → Data → FIN

UDP/DNS:
Query → Response
```

## 🎯 Next

**Day 39 — DNS + HTTP Packet Analysis**

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
