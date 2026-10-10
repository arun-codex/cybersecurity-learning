# 🗺️ Roadmap Status

## ✅ Completed through Day 40

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
- TCP SYN, SYN/ACK and ACK
- Three-way handshake
- TCP data and PSH + ACK
- TCP FIN + ACK termination
- Client/server port analysis
- TCP payload length analysis

### UDP/DNS completed
- UDP DNS query and response for `example.com`
- UDP source/destination ports
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
- Hostname: `example.com`, type A
- Transaction ID: `0x46c4`
- Response: No error
- A records: `104.20.23.154`, `172.66.147.243`
- Response time: ~69.4 ms

### HTTP completed
- Local Python HTTP server on port 8000; capture on loopback `lo`
- TCP SYN → SYN/ACK → ACK
- `GET / HTTP/1.1`
- Host: `127.0.0.1:8000`
- User-Agent: `curl/8.18.0`
- HTTP `200 OK`, Content-Type `text/html`, Content-Length `19`

## 🟢 Day 40 — TLS + HTTPS Analysis

**Status: ✅ Completed — practical capture, SOC mini-investigation, and final active recall passed (3.5/4).**

### Client Hello
- Used `curl https://example.com` to generate HTTPS traffic
- Client source port `50804` → server port `443`
- SNI: `example.com`
- Client advertised TLS 1.2 and TLS 1.3 via `supported_versions`
- Wireshark listed 35 offered cipher suites
- Observed `server_name`, ALPN and `key_share` extensions

### Server Hello
- Server source port `443` → client destination port `50804`
- Negotiated TLS 1.3 indicated by `supported_versions` (`0x0304`)
- Cipher suite: `TLS_AES_256_GCM_SHA384` (`0x1302`)
- Key-share information included `X25519MLKEM768`
- Lesson: Client Hello offers options; Server Hello identifies selected parameters. Do not interpret the legacy version field in isolation.

### Encrypted application data
- Observed TLS Application Data record type 23
- TLS record data length: 3,853 bytes
- Reassembled TCP data: 3,858 bytes across two segments (3,651 + 207 bytes)
- Selected frame: 293 bytes on wire with 207 bytes TCP payload
- Could not read the HTTP page content from the encrypted payload without appropriate TLS secrets

### Certificate filter
- Tried `tls.handshake.type == 11`
- 103 packets captured; zero matched the filter in that view
- This is consistent with TLS 1.3 post-Server-Hello handshake messages being encrypted without session secrets. Zero matches does not prove that no certificate was sent.

### SOC evidence exercise
Identified evidence to investigate:
1. Client/server IPs — communicating hosts
2. Client/server ports — endpoints and likely service
3. Packet sizes/data volume — unusual transfer patterns
4. DNS activity — hostname/IP relationship and query history; correlate with actual connections
5. Connection frequency — compare against normal application/device behavior and inspect surrounding evidence

HTTPS or frequent connections alone do not prove malicious activity.

### Final active recall — passed (3.5/4)
- **TCP vs TLS:** TCP establishes the transport connection and provides reliable, ordered delivery; the TCP three-way handshake is used to establish the connection. TLS protects application communication through encryption, integrity and authentication.
- **Sequence:** TCP connection → TLS handshake → encrypted application traffic.
- **Certificate visibility:** TLS 1.3 encrypts the Certificate message after Server Hello; without appropriate session secrets, Wireshark may not decode it as a Certificate.
- **SOC reasoning:** 200 HTTPS connections in 10 minutes is a reason to investigate, not proof of maliciousness. Compare with normal behavior and inspect timing, traffic volume, DNS history and endpoint telemetry when available.

## 🟡 Day 41 — Wireshark Filters

**Status: 🟡 In progress — practical challenge findings recorded in `notes/day41-filters.md`; final review pending.**

### Display filters practiced
- `dns`: 2 packets — query and response for `example.com` (AAAA)
- `ip.dst == 192.168.1.9`: 3 packets
- `ip.src == 192.168.1.9`: 5 packets
- `ip.addr == 192.168.1.9`: 8 IPv4 packets
- `tcp.port == 443`: 72 packets
- `udp.port == 53`: 2 packets
- `tcp.flags.syn == 1`: 2 packets; initial SYN filter: 1 packet
- `tcp.flags.reset == 1`: 0 packets
- `tcp.analysis.retransmission`: 0 packets
- `tcp.analysis.duplicate_ack`: 0 packets
- `tls`: 28 packets

### Analysis tools
- Followed `tcp.stream eq 3`; approximately 10 KB of encrypted conversation data was reassembled.
- IPv4 top endpoint: `192.168.1.9` with 8 packets / ~1 KB.
- Top IPv6 endpoint shown: `2401:4900:88b4:91a:d6fe:fa54:f22b:c5a5`, 89 packets / ~46 KB.
- TCP Conversations: 9 conversations; top by packets = 25 packets / 11 KB (stream 6); top by bytes = 17 KB / 20 packets (stream 4).
- DNS over UDP: `192.168.1.9:48606` ↔ `192.168.1.1:53`, 2 packets / 192 bytes.

### Core lesson
`tcp.port == 443` matches TCP packets based on port; `tls` matches packets Wireshark dissects as TLS. Packet counts are not connection counts. Zero matching retransmission/RST/duplicate-ACK packets in this capture do not prove those events never occur.

See [`notes/day41-filters.md`](notes/day41-filters.md) for the Top 10 filters and detailed results.

## 🎯 Current next step

**Finish Day 41 review / recall, then move to Day 42.**

## 🧠 Analyst mindset

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
