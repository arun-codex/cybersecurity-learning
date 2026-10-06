# 📅 Day 37 — Ethernet + IP Analysis

**Status:** 🟡 In Progress

## 🎯 Goal

Connect previous networking knowledge with real packets.

## ✅ What I Studied So Far

I used Wireshark to inspect real Ethernet, IPv4, TCP and ICMP packets.

### 🟦 Ethernet / Link Layer

For an IPv4 ICMP Echo Request, I identified:

```text
Source MAC:
de:2f:33:bc:53:d7

Destination MAC:
30:bd:13:f4:21:b8

EtherType:
IPv4 (0x0800)
```

### 🌐 IPv4 Layer

Observed:

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

### 🔵 ICMP

The packet was identified as:

```text
Type:
Echo (ping) request (8)

Code:
0
```

The capture showed a ping request from my machine to `1.1.1.1`.

### 🧠 Important Layer Distinction

```text
Ethernet frame
    ↓
EtherType = IPv4 (0x0800)
    ↓
IPv4 packet
    ↓
Protocol = ICMP (1)
    ↓
ICMP Echo Request
```

### 📦 Frame Length vs IP Total Length

The capture showed:

```text
Frame Length:
98 bytes

IPv4 Total Length:
84 bytes
```

This taught me that the captured Ethernet frame is larger than the IPv4 packet because the frame also contains the Ethernet header.

### 🔵 Earlier TCP Observation

I also practiced reading a TCP SYN packet:

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

## ✅ Day 37 Skills Practiced

- Source MAC
- Destination MAC
- EtherType
- Source IP
- Destination IP
- IPv4 version
- TTL
- Protocol
- IPv4 total length
- ICMP Echo Request
- Wireshark packet details
- Difference between frame length and IP packet total length

## ⏳ Still To Do

According to the Day 37 plan:

- Capture/analyze additional IPv4 packets
- Use `ip.addr == 1.1.1.1`
- Use `ip.src == YOUR_IP`
- Document 3 packets
- Inspect the ICMP Echo Reply from `1.1.1.1`
- Answer the SOC questions:
  - Who initiated the communication?
  - What protocol was used?
  - Was there a response?
  - How frequently did it happen?
  - What evidence do I have?
- Finish the Day 37 definition of done

## 📌 Current Assessment

**Partially completed — do not mark Day 37 complete yet.**

I have now completed the core Ethernet + IPv4 field identification exercise. The next task is to inspect the Echo Reply and then complete the SOC analysis/documentation.
