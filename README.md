# 🛡️ Cybersecurity Learning

My hands-on cybersecurity learning journey focused on Networking, Linux, SOC / Blue Team, security analysis, and practical labs.

## 🎯 Current Goal
- **Target:** Cybersecurity / SOC / Blue Team internship
- **Progress:** **Days 1–42 ✅ Complete**
- **Latest completed milestone:** Week 6 — Wireshark
- **Current week:** Week 7 — Nmap + Network Enumeration (planned; Day 43 not yet complete)
- **Full plan:** [Week 7 Days 43–49](week-7/week-7-nmap-network-enumeration.md)
- **Previous-week review:** [Week 6 retrospective — Me vs. Me](week-6/week-6-retrospective.md)
- **Next:** Day 43 — Nmap installation, purpose + first localhost scan

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

### Day 41 ✅ Complete — Wireshark Filters
- Practiced DNS, IPv4 address, TCP/UDP port, SYN, RST, retransmission, duplicate ACK and TLS display filters
- Used Follow TCP Stream on `tcp.stream eq 3`
- Examined IPv4/IPv6 Endpoints and TCP/UDP Conversations
- Week 6 day file: [`week-6/day-41-filters-streams-endpoints.md`](week-6/day-41-filters-streams-endpoints.md)
- Filter cheat sheet: [`week-6/wireshark-filters.md`](week-6/wireshark-filters.md)
- Detailed filter results: [`notes/day41-filters.md`](notes/day41-filters.md)
- **Active recall passed:** explained that `tls` can show handshake packets as well as application-data packets; distinguished protocol filtering from TCP port filtering
- **Result:** completed practical filters, Follow TCP Stream, Endpoints, Conversations, and evidence notes

## Day 42 ✅ Complete — Mini SOC Wireshark Investigation
- Week 6 day file: [`week-6/day-42-wireshark-investigation.md`](week-6/day-42-wireshark-investigation.md)
- Full investigation report: [`investigations/day42-wireshark-investigation.md`](investigations/day42-wireshark-investigation.md)
- Controlled localhost lab: 20 initial SYN packets and 20 RST responses; 40 packets matched `tcp.port == 9999` in a 52-packet capture
- Verified DNS query/response, TCP three-way handshake, UDP/QUIC traffic, local HTTP GET/200 OK, and TLS Client Hello/Server Hello across separate captures
- Reused documented Day 41 evidence for Endpoints, Conversations and Follow TCP Stream
- Theory test: **7.75/10**; passed with targeted correction of endpoint/conversation terminology
- **Week 6 practical checklist completed across multiple captures**; see the day file and full investigation report
- **Week 6 retrospective:** [Completed goals, personal feedback and Week 7 improvement plan](week-6/week-6-retrospective.md)

## 🧭 Week 7 — Nmap + Network Enumeration

**Status: Planned — tasks remain unchecked until demonstrated with actual commands, outputs and explanations.**

- [Full Days 43–49 plan](week-7/week-7-nmap-network-enumeration.md)
- [Week 6 retrospective and feedback](week-6/week-6-retrospective.md)
- Previous-week theory baseline: **7.75/10**
- Carry-forward focus: precise terminology (endpoint vs. conversation; FIN vs. RST), reading the exact selected packet, separating observation from interpretation, documenting limitations, and independent recall.

## 🎯 Next

**Day 43 — Nmap installation, purpose + first localhost scan**

## 🧪 Study Method
**Goal → prerequisites → needle movers → brief learning → practice → active recall → document**

## 🧠 Analyst Mindset

```text
Evidence → Observation → Hypothesis → More evidence → Conclusion
```

> Dates in the daily notes are roadmap/planned dates reconstructed from the weekday sequence. They are not claimed as verified study timestamps.
