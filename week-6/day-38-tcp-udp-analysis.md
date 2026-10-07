# 📅 Day 38 — TCP + UDP Packet Analysis

**Status:** 🟡 In Progress

## 🎯 Goal

Watch TCP happen inside Wireshark and compare it with UDP.

## 🔵 TCP Packet Analysis

### TCP Flags Studied

- SYN → connection establishment
- ACK → acknowledgment
- FIN → graceful termination
- RST → reset
- PSH → push available data toward the application

## 🔗 TCP Three-Way Handshake Observed

For one HTTPS TCP connection:

### 1. SYN

```text
Client:
2401:4900:8f72:20bf:dceb:744b:7ab9:bfbc

Server:
2603:1061:14:155::1

Source Port:
44566

Destination Port:
443

Flags:
SYN

TCP Data Length:
0 bytes
```

### 2. SYN/ACK

```text
Server:
2603:1061:14:155::1

Client:
2401:4900:8f72:20bf:dceb:744b:7ab9:bfbc

Source Port:
443

Destination Port:
44566

Flags:
SYN + ACK

Relative Sequence Number:
0

Relative Acknowledgment Number:
1

TCP Data Length:
0 bytes

MSS:
1230 bytes
```

### 3. ACK

An ACK-only packet was observed on another HTTPS TCP stream:

```text
Source Port:
46438

Destination Port:
443

Sequence:
1

Acknowledgment:
1

Flags:
ACK

SYN:
Not set

FIN:
Not set

RST:
Not set

TCP Data Length:
0 bytes
```

### Mental Model

```text
SYN
  ↓
SYN + ACK
  ↓
ACK

= TCP connection establishment
```

## 📦 TCP Data Observed

A separate TCP stream contained an application-data packet:

```text
Source:
192.168.1.9

Destination:
192.168.1.4

Source Port:
51582

Destination Port:
8009

Sequence Number:
1

Acknowledgment Number:
1

Flags:
PSH + ACK

TCP Segment Length:
110 bytes
```

### What happened?

An established TCP connection carried **110 bytes of TCP payload data**.

Important distinction:

```text
Handshake packets:
TCP Segment Len = 0

Data packet:
TCP Segment Len = 110
```

The PSH + ACK flags show that the packet both acknowledged received data and carried application data.

## 🔴 TCP Termination Observed

For the HTTPS stream using client port **46438**:

```text
Source Port:
46438

Destination Port:
443

Sequence Number:
1930

Acknowledgment Number:
6465

Flags:
FIN + ACK

TCP Segment Length:
0 bytes
```

### What happened?

The client sent a **FIN + ACK** packet to begin gracefully closing its side of the TCP connection.

- FIN = finished sending on this side
- ACK = acknowledges received data
- RST was not used in this packet

A FIN consumes one sequence number, so the next acknowledgment for this FIN would normally advance by one.

## 🧠 TCP Lifecycle Observed

```text
Connection establishment
        ↓
SYN
        ↓
SYN + ACK
        ↓
ACK
        ↓
TCP data
        ↓
FIN + ACK
        ↓
Connection termination
```

## 🟠 UDP / DNS

**Not studied yet in this session.**

Planned next practical:

```bash
dig example.com
```

Wireshark filters:

```text
udp
dns
```

Remaining UDP work:
- Find UDP DNS query
- Identify client/server
- Identify source/destination ports
- Explain that UDP has no TCP-style handshake
- Compare TCP and UDP

## 📌 Current Progress

### ✅ Completed
- TCP SYN
- TCP SYN/ACK
- TCP ACK
- TCP data
- FIN + ACK
- TCP flags: SYN, ACK, FIN, RST, PSH
- TCP connection establishment
- TCP termination
- Client/server port analysis
- TCP payload length vs TCP options

### ⏳ Remaining Day 38
- UDP DNS query
- TCP vs UDP comparison
- Final Day 38 notes / definition of done

## 🛡️ Analyst Mindset

Use the packet evidence first:

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

> This note records the TCP work actually observed during the session. UDP work is intentionally left pending until it is studied.
