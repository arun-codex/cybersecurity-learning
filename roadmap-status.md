# 🗺️ Roadmap Status

## ✅ Completed through Day 35

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

## 🦈 Current — Day 36: Wireshark Basics

**Status: 🟡 In progress**

### Completed in Day 36 so far
- Started Wireshark capture
- Captured own traffic on `wlp0s20f3`
- Generated DNS traffic with `dig example.com`
- Applied the `dns` display filter
- Inspected a DNS response
- Identified UDP port 53
- Identified client temporary port 58431
- Identified an AAAA query for `example.com`
- Observed a successful DNS response with one answer
- Recorded approximately 67 ms response time

### Remaining Day 36
ICMP → TCP → TLS → save PCAPNG → complete notes.

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
