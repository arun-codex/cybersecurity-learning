# 🛡️ Cybersecurity Learning

My hands-on cybersecurity learning journey focused on Networking, Linux, SOC / Blue Team, security analysis, and practical labs.

## 🎯 Current Goal
- **Target:** Cybersecurity / SOC / Blue Team internship
- **Primary environment:** Fedora Linux
- **Progress:** **Day 36 — Wireshark Basics in progress**
- **Completed:** Days 1–35
- **Current milestone:** Week 6 — Wireshark
- **Next:** Complete Day 36, then continue Day 37 — Ethernet + IP analysis

## 📚 Learning Path

```text
Week 1  → Networking fundamentals
Week 2  → DNS, TCP/UDP, HTTP/HTTPS, traffic flow
Week 3  → Linux fundamentals
Week 4  → Networking + Linux integration
Week 5  → Security fundamentals + attacks + MITRE ATT&CK
Week 6  → Wireshark / packet analysis
```

## ✅ Completed

### Week 1 — Networking
- OSI model
- TCP/IP model
- IPv4 and subnetting
- Ports and protocols

### Week 2 — Network Traffic
- DNS
- TCP vs UDP
- HTTP
- HTTPS / TLS
- Browser-to-server traffic flow

### Week 3 — Linux
- Linux filesystem
- Core terminal commands
- grep / find
- Permissions
- Users and groups
- Processes and services
- sudo
- Pipes
- Redirection
- Command chaining

### Week 4 — Integration
- ping
- traceroute
- firewalld / firewall concepts
- `ss`
- Network troubleshooting

### Week 5 — Security Fundamentals
- CIA Triad
- AAA
- Least privilege
- Defense in depth
- Threat / vulnerability / exploit / risk
- IOC / TTP
- Phishing
- Brute force
- Password spraying
- Malware
- Credential theft
- MITRE ATT&CK basics
- Mini SOC investigation

## 🦈 Week 6 — Wireshark (In Progress)

### Day 36
Started practical packet analysis using my own traffic.

First completed investigation:
- Wireshark 4.6.9
- Interface: `wlp0s20f3`
- DNS display filter
- UDP port 53
- Client temporary port 58431
- AAAA query for `example.com`
- Successful DNS response with one answer
- Approx. 67 ms response time

Remaining Day 36 work:
- ICMP
- TCP
- TLS
- Save PCAPNG
- Finish notes

## 🧪 Study Method
**Concept → Practical → SOC connection → Active recall**

## 🧠 Analyst Mindset

```text
Evidence → Observation → Hypothesis → More evidence → Conclusion
```

> Dates in the daily notes are roadmap/planned dates reconstructed from the weekday sequence. They are not claimed as verified study timestamps.
