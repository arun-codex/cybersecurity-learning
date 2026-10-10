# 🛡️ Cybersecurity Learning

My hands-on cybersecurity learning journey focused on Networking, Linux, SOC / Blue Team, security analysis, and practical labs.

## 🎯 Current Goal
- **Target:** Cybersecurity / SOC / Blue Team internship
- **Progress:** **Days 1–40 ✅ Complete**
- **Current milestone:** Week 6 — Wireshark
- **Next:** Day 41 — continue Week 6 packet analysis

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
- SYN, SYN/ACK, ACK
- Three-way handshake
- TCP data, PSH + ACK
- FIN + ACK and termination
- Client/server ports

UDP/DNS:
- UDP source/destination ports
- DNS query and response for `example.com`
- Transaction ID matching
- A records
- No TCP-style handshake for the observed DNS exchange

### Day 39 ✅ Complete
DNS:
- DNS query/response capture
- `dns` filter and `dns.qry.name == "example.com"`
- Client/server IP and port analysis
- Transaction ID `0x46c4`
- Successful DNS response
- A records `104.20.23.154` and `172.66.147.243`
- ~69.4 ms response time

HTTP:
- Local Python HTTP server
- Loopback capture on `lo`
- TCP three-way handshake
- HTTP GET request, Host header and User-Agent
- HTTP 200 OK, Content-Type and Content-Length

### Day 40 ✅ Complete — TLS + HTTPS Analysis
- Captured HTTPS traffic generated with `curl https://example.com`
- Identified Client Hello and SNI `example.com`
- Observed advertised TLS 1.2 / TLS 1.3 support
- Identified Server Hello, negotiated TLS 1.3 and `TLS_AES_256_GCM_SHA384`
- Inspected encrypted application data and compared frame, TCP payload and TLS record lengths
- Tested the Certificate display filter; no decoded matches in the current view, which does not prove a certificate was absent
- Completed a SOC evidence exercise: IPs, ports, packet/data sizes, DNS activity and connection frequency
- **Active recall passed:** explained TCP vs TLS, ordered TCP → TLS handshake → encrypted application traffic, explained TLS 1.3 Certificate visibility, and correctly avoided declaring frequent HTTPS connections malicious without more evidence
- **Result:** 3.5/4 — passed

### Day 41 🟡 In progress — Wireshark Filters
- Practiced DNS, IPv4 address, TCP/UDP port, SYN, RST, retransmission, duplicate ACK and TLS display filters
- Used Follow TCP Stream on `tcp.stream eq 3`
- Examined IPv4/IPv6 Endpoints and TCP/UDP Conversations
- Saved evidence and Top 10 filters in [`notes/day41-filters.md`](notes/day41-filters.md)
- **Status:** practical challenge documented; keep Day 41 in progress until final review / recall is complete

## 🎯 Next

**Finish Day 41 review, then continue to Day 42**

## 🧪 Study Method
**Goal → prerequisites → needle movers → brief learning → practice → active recall → document**

## 🧠 Analyst Mindset

```text
Evidence → Observation → Hypothesis → More evidence → Conclusion
```

> Dates in the daily notes are roadmap/planned dates reconstructed from the weekday sequence. They are not claimed as verified study timestamps.
