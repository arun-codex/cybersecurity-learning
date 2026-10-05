# 🦈 Day 36 — Wireshark Basics

**Planned date:** 2026-09-28  
**Status:** ✅ Completed

## 🎯 Goal

Learn basic packet capture and start reading real network traffic in Wireshark.

Day 36 focus:
- Packet capture
- Packet List
- Packet Details
- Packet Bytes
- DNS traffic
- ICMP/ICMPv6 traffic
- TCP traffic
- TLS traffic

## ⚙️ Lab Environment

- Wireshark version: **4.6.9**
- Capture interface: **wlp0s20f3**
- Lab type: **Own computer / own traffic**
- Capture filter: none

## 🧪 Traffic Generated

Commands used:

```bash
ping -c 4 example.com
dig example.com
curl -I https://example.com
```

## 🔎 DNS Investigation

Display filter:

```
dns
```

### Observation

A DNS response packet was inspected in Wireshark.

```text
Protocol: UDP
Source Port: 53
Destination Port: 58431
DNS Type: Response
Query: AAAA example.com
Result: No error
Answer RRs: 1
Transaction ID: 0x5ea4
Response time: ~67 ms
```

### Address flow observed

```text
DNS query:
Local host : 58431
      ↓ UDP
DNS server : 53

DNS response:
DNS server : 53
      ↓ UDP
Local host : 58431
```

### What happened?

My computer requested the **AAAA record** for `example.com`.

The DNS server replied over **UDP port 53** with **one IPv6 answer** and a successful / No error response.

### What I learned

- DNS traffic was observed over UDP port **53**.
- The client used a temporary source port.
- The response returned from server port **53** to the client port.
- **AAAA** was used to request an IPv6 address.
- The DNS **Transaction ID** helped identify the query/response pair.
- Wireshark exposed the packet structure behind the DNS lookup.

## 🔵 ICMP / ICMPv6 Investigation

Display filter used:

```
icmpv6
```

### Observation

An **ICMPv6 Echo (ping) request** was captured.

Observed values:

```text
Protocol: ICMPv6
Type: Echo (ping) request (128)
Code: 0
Sequence: 1
Identifier: 0x5f61
Hop Limit: 64
Data: 40 bytes
Response: Echo (ping) reply observed
Approx. response time: 46.87 ms
```

### What happened?

My computer sent an ICMPv6 Echo Request to the remote IPv6 destination and received a corresponding Echo Reply.

This demonstrates the packet-level form of the `ping` command.

## 🔵 TCP Investigation

Filters used:

```
tcp
```

Initial SYN:

```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

SYN/ACK:

```
tcp.flags.syn == 1 && tcp.flags.ack == 1
```

### Observed TCP connection

Client port:

```
50576
```

Server port:

```
443
```

### Three-way handshake

```text
Client                         Server

50576 ───── SYN ─────────────> 443
50576 <──── SYN + ACK ─────── 443
50576 ───── ACK ─────────────> 443
```

### Packet observations

**SYN**
- Source port: **50576**
- Destination port: **443**
- SYN set
- Relative sequence number: **0**
- TCP payload length: **0 bytes**

**SYN/ACK**
- Source port: **443**
- Destination port: **50576**
- SYN and ACK set
- Relative sequence number: **0**
- Acknowledgment number: **1**
- TCP payload length: **0 bytes**

**Final ACK**
- Source port: **50576**
- Destination port: **443**
- ACK set
- Relative sequence number: **1**
- Acknowledgment number: **1**
- TCP payload length: **0 bytes**

### TCP data

The same TCP stream then carried TLS traffic.

Stream observed:

```
tcp.stream == 6
```

After the handshake, TLS packets appeared on the established TCP connection.

### What happened?

A TCP connection to the HTTPS server was successfully established using the standard SYN → SYN/ACK → ACK process. The connection then carried higher-layer TLS traffic.

## 🔐 TLS Investigation

Display filter:

```
tls
```

### Client Hello

A **TLS Client Hello** was captured.

Observed:

```text
Source port: 50576
Destination port: 443
Handshake: Client Hello
SNI: example.com
Cipher suites: 35 offered
Supported versions: TLS 1.3, TLS 1.2 shown
ALPN extension: present
```

### What happened?

After TCP connection establishment, my computer sent a TLS Client Hello to the HTTPS server.

The Client Hello contained the requested hostname `example.com`, supported TLS information, cipher suites, and other extensions.

The capture then showed:

```text
TCP handshake
      ↓
TLS Client Hello
      ↓
TLS Server Hello / Change Cipher Spec
      ↓
TLS Application Data
```

### Important observation

The application traffic was shown as TLS **Application Data** rather than readable HTTP content, demonstrating that the higher-layer application traffic was protected by TLS.

## 🧠 Day 36 Final Mental Model

```text
DNS
 ↓
TCP SYN
 ↓
TCP SYN/ACK
 ↓
TCP ACK
 ↓
TLS Client Hello
 ↓
TLS Server Hello
 ↓
Encrypted Application Data
```

At the packet layer:

```text
Ethernet
   ↓
IP / IPv6
   ↓
TCP / UDP / ICMPv6
   ↓
Application / TLS protocols
```

## 🛡️ Analyst Mindset

```text
Evidence
   ↓
Observation
   ↓
Hypothesis
   ↓
More Evidence
   ↓
Conclusion
```

Do not immediately label unusual traffic as an attack. First identify what the packets actually show.

## ✅ Day 36 Definition of Done

- ✅ Start Wireshark
- ✅ Identify active network interface
- ✅ Perform basic packet capture
- ✅ Identify DNS traffic
- ✅ Identify ICMP/ICMPv6 traffic
- ✅ Identify TCP traffic
- ✅ Recognize TCP three-way handshake
- ✅ Identify TCP source/destination ports
- ✅ Identify TLS traffic
- ✅ Identify TLS Client Hello
- ✅ Understand Packet List / Packet Details / Packet Bytes
- ✅ Connect Ethernet/IP → TCP/UDP → application/TLS
- ✅ Analyze own traffic using Wireshark

## ⏳ File / Documentation

PCAPNG should be saved locally as:

```text
pcaps/day36-basic-capture.pcapng
```

> PCAP files are kept local unless verified to contain nothing sensitive.

## 📝 Final Reflection

Day 36 connected my previous networking knowledge with real packet captures. I can now look at a capture and identify who communicated, which protocol was used, which ports were involved, and what happened at the packet level.

