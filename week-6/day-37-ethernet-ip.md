# 📅 Day 37 — Ethernet + IP Analysis

**Status:** ✅ Completed

## 🎯 Goal

Connect previous networking knowledge with real packets.

## ✅ Packet Analysis Completed

### Packet 1 — IPv6 TCP SYN

I practiced reading an IPv6 TCP SYN packet:

```text
Source IPv6:
2401:4900:88b4:91a:fd6e:fa54:f22b:c5a5

Destination IPv6:
2606:4700:90d5:72db:f2c5:8ba:ef6b:ff98

Source Port:
48506

Destination Port:
443

TCP Flag:
SYN

Frame Length:
94 bytes

TCP Data Length:
0 bytes
```

**What happened:** My computer initiated a TCP connection toward an HTTPS service on port 443.

**Why it matters:** It connected the earlier TCP theory to a real packet and reinforced source/destination ports and TCP flags.

### Packet 2 — IPv4 ICMP Echo Request

Ethernet:

```text
Source MAC:
de:2f:33:bc:53:d7

Destination MAC:
30:bd:13:f4:21:b8

EtherType:
IPv4 (0x0800)
```

IPv4:

```text
Source IP:
192.168.1.9

Destination IP:
1.1.1.1

TTL:
64

Protocol:
ICMP (1)

Total Length:
84 bytes
```

ICMP:

```text
Type:
Echo (ping) request (8)

Code:
0
```

**What happened:** My machine sent an ICMP Echo Request to 1.1.1.1.

**Why it matters:** It demonstrated the relationship between Ethernet → IPv4 → ICMP in a real packet.

### Packet 3 — IPv4 ICMP Echo Reply

```text
Source IP:
1.1.1.1

Destination IP:
192.168.1.9

TTL:
58

Protocol:
ICMP (1)

Total Length:
84 bytes

Type:
Echo (ping) reply (0)

Code:
0

Sequence:
5

Response time:
~42 ms
```

Wireshark associated the reply with its corresponding request.

**What happened:** 1.1.1.1 replied to my ICMP Echo Request.

**Why it matters:** The reply provides direct packet evidence that the destination responded.

## 🧠 Important Layer Distinction

```text
Ethernet frame
    ↓
EtherType = IPv4 (0x0800)
    ↓
IPv4 packet
    ↓
Protocol = ICMP (1)
    ↓
ICMP Echo Request / Reply
```

## 📦 Frame Length vs IP Total Length

Observed on the IPv4 ICMP request:

```text
Frame Length:
98 bytes

IPv4 Total Length:
84 bytes
```

The Ethernet frame is larger because the captured frame contains the Ethernet header in addition to the IPv4 packet.

## 🕵️ SOC Questions

### Who initiated the communication?

```text
192.168.1.9
```

Evidence: the first packet was an ICMP Echo Request from 192.168.1.9 to 1.1.1.1.

### What protocol was used?

```text
IPv4 + ICMP
```

Specifically:
- Echo Request = ICMP Type 8
- Echo Reply = ICMP Type 0

### Was there a response?

**Yes.**

Evidence:
- Source: 1.1.1.1
- Destination: 192.168.1.9
- ICMP Type 0 Echo Reply
- Response time for the selected packet: approximately 42 ms

### How frequently did it happen?

The capture contained **5 ICMP Echo Replies**, matching the `ping -c 5 1.1.1.1` test.

### What evidence do I have?

- ICMP Echo Request packets from 192.168.1.9 to 1.1.1.1
- ICMP Echo Reply packets from 1.1.1.1 to 192.168.1.9
- Matching request/reply relationship in Wireshark
- Five replies observed
- Packet-level source, destination, protocol, TTL and length values

## 🧠 Analyst Mindset

Do not immediately say:

> "This is an attack."

First collect evidence.

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

## ✅ Day 37 Definition of Done

- ✅ Source MAC
- ✅ Destination MAC
- ✅ EtherType
- ✅ Source IP
- ✅ Destination IP
- ✅ IPv4 TTL
- ✅ Protocol
- ✅ IPv4 total length
- ✅ ICMP Echo Request
- ✅ ICMP Echo Reply
- ✅ Documented packet observations
- ✅ Answered SOC investigation questions

## 📝 Reflection

Day 37 connected Ethernet and IPv4 theory with real Wireshark packets. I can now move from a packet list to the actual fields, identify who communicated, determine the protocol and direction, and use packet evidence to explain what happened.

