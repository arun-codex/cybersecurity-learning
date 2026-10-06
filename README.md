# 🛡️ Cybersecurity Learning

My hands-on cybersecurity learning journey focused on Networking, Linux, SOC / Blue Team, security analysis, and practical labs.

## 🎯 Current Goal
- **Target:** Cybersecurity / SOC / Blue Team internship
- **Primary environment:** Fedora Linux
- **Progress:** **Day 37 — Ethernet + IP Analysis in progress**
- **Completed:** Days 1–36
- **Current milestone:** Week 6 — Wireshark
- **Next:** Inspect the IPv4 ICMP Echo Reply and finish Day 37

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

## 🦈 Week 6 — Wireshark

### Day 36 ✅ Complete
Practical packet analysis using my own traffic on `wlp0s20f3`.

Analyzed:
- DNS response
- ICMPv6 ping request/reply
- TCP three-way handshake
- TCP traffic on port 443
- TLS Client Hello
- TLS application data

### Day 37 🟡 In Progress
Completed core Ethernet + IPv4 field identification on an ICMP Echo Request.

Observed:

```text
Source MAC      de:2f:33:bc:53:d7
Destination MAC 30:bd:13:f4:21:b8
EtherType        IPv4 (0x0800)

Source IP        192.168.1.9
Destination IP   1.1.1.1
TTL              64
Protocol         ICMP (1)
Total Length     84 bytes
ICMP Type        Echo Request (8)
```

Also learned the distinction between:
- Ethernet frame length
- IPv4 total length
- TCP data length

Remaining Day 37:
- Inspect ICMP Echo Reply
- Finish SOC questions
- Document 3 packets
- Complete Day 37

## 🧪 Study Method
**Concept → Practical → SOC connection → Active recall**

## 🧠 Analyst Mindset

```text
Evidence → Observation → Hypothesis → More evidence → Conclusion
```

> Dates in the daily notes are roadmap/planned dates reconstructed from the weekday sequence. They are not claimed as verified study timestamps.
