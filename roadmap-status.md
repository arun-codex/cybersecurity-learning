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

### Key packet observations
- DNS: UDP source/destination ports **53 ↔ 58431**
- DNS: **AAAA example.com**
- ICMPv6: Echo Request / Echo Reply
- TCP: **50576 → 443**
- TCP handshake: **SYN → SYN/ACK → ACK**
- TLS: **Client Hello**, SNI **example.com**
- TLS Application Data observed after the handshake

## 🎯 Next

**Day 37 — Ethernet + IP Analysis**

Then continue:
TCP/UDP → DNS/HTTP → TLS → filters → streams → endpoints → conversations → mini SOC investigation.

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
