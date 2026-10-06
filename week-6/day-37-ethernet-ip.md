# 📅 Day 37 — Ethernet + IP Analysis

**Status:** 🟡 In Progress

## 🎯 Goal

Connect previous networking knowledge with real packets.

## ✅ What I Studied So Far

I used Wireshark to inspect a real TCP packet and practiced identifying the Ethernet and IP-layer fields.

### 🟦 Ethernet / Link Layer

I was able to identify:

- Source MAC
- Destination MAC
- Ethernet II / EtherType information

### 🌐 IP Layer

I was able to identify:

- Source IP
- Destination IP
- IP version
- Protocol

### 🔵 Example Packet Observed

```text
Source IP:
2401:4900:88b4:91a:fd6e:fa54:f22b:c5a5

Destination IP:
2606:4700:90d5:72db:f2c5:8ba:ef6b:ff98

Protocol:
TCP

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

### 🧠 Important correction learned

```text
Frame Length = total captured frame size

TCP Data Length = actual TCP payload

For this SYN packet:
Frame Length = 94 bytes
TCP Data Length = 0 bytes
```

The packet was an **IPv6** packet, so I have not yet completed the Day 37 IPv4-specific exercise.

## ⏳ Still To Do

According to the Day 37 plan:

- Capture an IPv4 ping to `1.1.1.1`
- Analyze with `icmp`
- Use `ip.addr == 1.1.1.1`
- Use `ip.src == YOUR_IP`
- Identify IPv4 TTL
- Identify IPv4 total length
- Document 3 packets
- Answer the SOC questions
- Finish the Day 37 definition of done

## 🕵️ SOC Questions Still Pending

- Who initiated the communication?
- What protocol was used?
- Was there a response?
- How frequently did it happen?
- What evidence do I have?

## 📌 Current Assessment

**Partially completed — do not mark Day 37 complete yet.**

I have practiced identifying Ethernet and IP information, but I still need the planned IPv4 packet-analysis exercise.
