# 🛡️ Cybersecurity Learning

My hands-on cybersecurity learning journey focused on Networking, Linux, SOC / Blue Team, security analysis, and practical labs.

## 🎯 Current Goal
- **Target:** Cybersecurity / SOC / Blue Team internship
- **Primary environment:** Fedora Linux
- **Progress:** **Day 39 ✅ Complete**
- **Completed:** Days 1–39
- **Current milestone:** Week 6 — Wireshark
- **Next:** Day 40 — TLS Analysis

## 📚 Learning Path

```text
Week 1  → Networking fundamentals
Week 2  → DNS, TCP/UDP, HTTP/HTTPS, traffic flow
Week 3  → Linux fundamentals
Week 4  → Networking + Linux integration
Week 5  → Security fundamentals + attacks + MITRE ATT&CK
Week 6  → Wireshark / packet analysis
```

## 🦈 Week 6 — Wireshark

### Day 36 ✅ Complete
- DNS response
- ICMPv6 ping request/reply
- TCP three-way handshake
- TCP traffic on port 443
- TLS Client Hello
- TLS application data

### Day 37 ✅ Complete
- Ethernet + IPv4 packet analysis
- Source/destination MAC
- EtherType
- IPv4 source/destination
- TTL
- ICMP request/reply
- SOC evidence questions

### Day 38 ✅ Complete
TCP:
- SYN
- SYN/ACK
- ACK
- Three-way handshake
- TCP data
- PSH + ACK
- FIN + ACK
- TCP termination
- Client/server ports

UDP/DNS:
- UDP source/destination ports
- DNS query for `example.com`
- DNS response
- Transaction ID matching
- A records
- No TCP-style handshake

### Day 39 ✅ Complete
DNS:
- DNS query/response capture
- `dns` filter
- `dns.qry.name == "example.com"`
- Client/server IP and port analysis
- Transaction ID `0x46c4`
- Successful DNS response
- A records `104.20.23.154` and `172.66.147.243`
- ~69.4 ms response time

HTTP:
- Local Python HTTP server
- Loopback capture on `lo`
- TCP three-way handshake
- HTTP GET request
- Host header
- User-Agent
- HTTP 200 OK
- Content-Type
- Content-Length

## 🎯 Next

**Day 40 — TLS Analysis**

Focus:
- TLS packet identification
- Client Hello
- Server Hello
- Certificate
- Encrypted Application Data
- Observable TLS metadata

## 🧪 Study Method
**Concept → Practical → SOC connection → Active recall**

## 🧠 Analyst Mindset

```text
Evidence → Observation → Hypothesis → More evidence → Conclusion
```

> Dates in the daily notes are roadmap/planned dates reconstructed from the weekday sequence. They are not claimed as verified study timestamps.
