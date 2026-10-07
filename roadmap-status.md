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

## 🔵 Day 38 — TCP + UDP Packet Analysis

**Status: 🟡 In Progress**

### TCP completed
- TCP SYN
- TCP SYN/ACK
- TCP ACK
- Three-way handshake
- TCP data
- TCP FIN + ACK termination
- SYN/ACK/FIN/RST/PSH flag recognition
- Client/server port analysis
- TCP payload length analysis

### Observed examples

Handshake:
```text
SYN
SYN + ACK
ACK
```

TCP data:
```text
192.168.1.9:51582
        ↓
192.168.1.4:8009

PSH + ACK
TCP Segment Len = 110 bytes
```

Termination:
```text
46438 → 443
FIN + ACK
Seq = 1930
Ack = 6465
TCP Segment Len = 0
```

### UDP still pending
Next session:
```bash
dig example.com
```

Then:
```text
udp
dns
```

After that, complete the TCP vs UDP comparison and Day 38 definition of done.

## 🎯 Next

**UDP DNS analysis → TCP vs UDP comparison → Day 38 complete**

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
