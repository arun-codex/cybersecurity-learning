# 📅 Day 38 — TCP + UDP Packet Analysis

**Status:** ✅ Completed

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

### 3. Final ACK

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

A TCP stream contained:

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

## 🟠 UDP / DNS Analysis

### DNS Query

Observed UDP DNS query:

```text
Source IP:
192.168.1.9

Destination IP:
192.168.1.1

Source Port:
53270

Destination Port:
53

Protocol:
UDP

DNS Query:
example.com

Record Type:
A

Transaction ID:
0x39df

Questions:
1

UDP payload:
40 bytes
```

### DNS Response

The corresponding response showed:

```text
Source IP:
192.168.1.1

Destination IP:
192.168.1.9

Source Port:
53

Destination Port:
53270

Transaction ID:
0x39df

Flags:
0x8180 — Standard query response, No error

Questions:
1

Answer RRs:
2

Additional RRs:
1

Response time:
~65.8 ms
```

The response returned two A records for `example.com`:

```text
104.20.23.154
172.66.147.243
```

### What happened?

My computer sent a UDP DNS query from temporary port **53270** to DNS server **192.168.1.1** on port **53** asking for the A record of `example.com`.

The DNS server returned a successful response with the same transaction ID and two IPv4 answers.

No TCP-style handshake was used for this DNS exchange.

## 🧠 TCP vs UDP Comparison

| TCP | UDP |
|---|---|
| Connection-oriented | Connectionless |
| TCP handshake | No TCP-style handshake |
| ACK / retransmission mechanisms | No TCP-style reliability |
| Ordered stream | Datagram based |
| More overhead | Lower overhead |

### Practical mental model

```text
🔵 TCP

SYN
 ↓
SYN/ACK
 ↓
ACK
 ↓
Data
 ↓
FIN


🟠 UDP / DNS

Query
 ↓
Response
```

## ✅ Day 38 Definition of Done

- ✅ Recognize SYN
- ✅ Recognize SYN/ACK
- ✅ Recognize ACK
- ✅ Recognize TCP connection establishment
- ✅ Identify TCP client/server ports
- ✅ Observe TCP data
- ✅ Recognize PSH + ACK
- ✅ Observe TCP termination with FIN + ACK
- ✅ Generate and analyze UDP DNS traffic
- ✅ Identify UDP source/destination ports
- ✅ Identify DNS query and response
- ✅ Compare TCP and UDP
- ✅ Understand that the DNS exchange used no TCP-style handshake

## 🛡️ Analyst Mindset

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

> This note records the packet analysis actually performed during the Day 38 lab.
