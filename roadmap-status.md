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

## 🌐 Day 37 — Ethernet + IP Analysis

**Status: 🟡 In Progress**

### Completed so far
- Identified Source MAC
- Identified Destination MAC
- Identified EtherType
- Identified IPv4 source/destination
- Identified TTL
- Identified protocol number
- Identified IPv4 total length
- Identified ICMP Echo Request
- Distinguished Ethernet frame length from IPv4 total length
- Practiced reading Wireshark packet details

### Observed ICMP Echo Request

```text
Source MAC:      de:2f:33:bc:53:d7
Destination MAC: 30:bd:13:f4:21:b8
EtherType:       IPv4 (0x0800)

Source IP:       192.168.1.9
Destination IP:  1.1.1.1
TTL:             64
Protocol:        ICMP (1)
Total Length:    84 bytes
ICMP Type:       Echo Request (8)
```

### Still pending
- Inspect ICMP Echo Reply from `1.1.1.1`
- Use `ip.addr == 1.1.1.1`
- Use `ip.src == YOUR_IP`
- Document 3 packets
- Answer the SOC questions
- Finish the Day 37 definition of done

## 🎯 Next

**Inspect the ICMP Echo Reply from 1.1.1.1**, then finish Day 37.

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
