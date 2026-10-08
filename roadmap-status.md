# 🗺️ Roadmap Status

## ✅ Completed through Day 39

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
- Transaction ID matching
- A records
- No TCP-style handshake for this DNS exchange

## 🟢 Day 39 — DNS + HTTP Packet Analysis

**Status: ✅ Completed**

### DNS completed
- Captured DNS query/response
- Used `dns` and `dns.qry.name == "example.com"`
- Client: `192.168.1.9:43052`
- DNS server: `192.168.1.1:53`
- Hostname: `example.com`
- Query type: A
- Transaction ID: `0x46c4`
- Response: No error
- A records: `104.20.23.154`, `172.66.147.243`
- Response time: ~69.4 ms
- Matched query and response using the transaction ID

### HTTP completed
- Created local Python HTTP server on port 8000
- Captured traffic on loopback interface `lo`
- Observed TCP SYN → SYN/ACK → ACK
- Analyzed `GET / HTTP/1.1`
- Host: `127.0.0.1:8000`
- User-Agent: `curl/8.18.0`
- HTTP response: `200 OK`
- Content-Type: `text/html`
- Content-Length: `19`

### Core lesson

```text
DNS:
Query → Response
Transaction ID → Correlation

HTTP:
TCP connection
   ↓
GET request
   ↓
200 OK response
```

## 🎯 Next

**Day 40 — TLS Analysis**

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
