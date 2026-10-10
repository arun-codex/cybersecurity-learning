# 🔎 Day 41 — Wireshark Filters

**Status: 🟡 In progress / practical challenge investigated; notes created from the Day 36 PCAP.**

## Goal

Reduce capture noise with display filters, inspect a TCP stream, and use Endpoints and Conversations statistics to identify important hosts and flows.

Capture used: `day36-basic-capture.pcapng` — 97 packets.

## ⭐ Top 10 Wireshark display filters

| # | Filter | Purpose |
|---:|---|---|
| 1 | `dns` | Show DNS packets |
| 2 | `tcp` | Show TCP packets |
| 3 | `udp` | Show UDP packets |
| 4 | `http` | Show packets Wireshark dissects as HTTP |
| 5 | `tls` | Show packets Wireshark dissects as TLS |
| 6 | `ip.addr == 192.168.1.9` | Match IPv4 packets where this address is source or destination |
| 7 | `tcp.port == 443` | Match TCP packets with source or destination port 443 |
| 8 | `udp.port == 53` | Match UDP packets using port 53 |
| 9 | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Find initial TCP SYN packets |
| 10 | `tcp.analysis.retransmission` | Show TCP packets Wireshark identifies as retransmissions |

### Other useful filters

```text
ip.src == 192.168.1.9
ip.dst == 192.168.1.9
tcp.flags.syn == 1
tcp.flags.reset == 1
tcp.analysis.duplicate_ack
tcp.stream eq 3
icmp
```

Note: the reset-flag field accepted in this Wireshark version is `tcp.flags.reset`, not `tcp.flags.rst`. Display filters only change which packets are shown; they do not delete packets from the capture. IPv4 filters beginning with `ip.` do not match IPv6 packets.

## Filter results from this capture

Total packets in the capture: **97**.

| Filter | Displayed | Observation |
|---|---:|---|
| `dns` | 2 | DNS query and response for `example.com` (AAAA query) |
| `ip.dst == 192.168.1.9` | 3 | IPv4 packets arriving at this host |
| `ip.src == 192.168.1.9` | 5 | IPv4 packets originating from this host |
| `ip.addr == 192.168.1.9` | 8 | IPv4 packets in either direction |
| `tcp.port == 443` | 72 | TCP packets using port 443, either direction |
| `udp.port == 53` | 2 | DNS over UDP, query and response |
| `tcp.flags.syn == 1` | 2 | One initial SYN and one SYN/ACK |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | 1 | Initial SYN |
| `tcp.flags.reset == 1` | 0 | No TCP reset packets matched |
| `tcp.analysis.retransmission` | 0 | No retransmissions identified by Wireshark |
| `tcp.analysis.duplicate_ack` | 0 | No duplicate ACKs identified by Wireshark |
| `tls` | 28 | Packets Wireshark dissects as TLS (28.9% of capture) |

The zero-count results mean that Wireshark did not identify matching packets in this particular 97-packet capture; they do not prove those events never happen on the network.

## Endpoint findings

### IPv4 tab
- `192.168.1.9`: 8 packets, approximately 1 KB; 5 transmitted packets / 566 bytes and 3 received packets / 462 bytes.
- `192.168.1.4`: 6 packets, 836 bytes.
- `192.168.1.1`: 2 packets, 192 bytes.

Among the displayed IPv4 endpoints, `192.168.1.9` had the most packets and bytes.

### IPv6 tab
- Highest IPv6 endpoint in the displayed table: `2401:4900:88b4:91a:d6fe:fa54:f22b:c5a5`
- 89 packets, approximately 46 KB; 42 transmitted / 30 KB and 47 received / 16 KB.

IPv4 and IPv6 should both be checked before deciding which endpoint is busiest across the full capture.

## Conversations findings

### TCP
The Conversations window displayed **9 TCP conversations**.

- Highest packet count: **25 packets / 11 KB**, stream ID 6, client port `50756` to destination port `443`.
- Highest byte total: **17 KB / 20 packets**, stream ID 4, client port `36890` to destination port `443`.

The most-packets conversation was not the most-bytes conversation. Port 443 commonly carries HTTPS/TLS, but the port number alone does not prove the application protocol.

### UDP / DNS
Found a DNS conversation:
- Client: `192.168.1.9:48606`
- DNS server: `192.168.1.1:53`
- 2 packets, 192 bytes total
- Client → server: 1 packet / 82 bytes
- Server → client: 1 packet / 110 bytes
- Duration: approximately 0.048 seconds
- DNS query type: AAAA for `example.com`

The two packet sizes (82 + 110 bytes) add up to the 192 bytes shown in the Conversations table.

## Follow TCP Stream

Followed `tcp.stream eq 3`.

- Wireshark reassembled the conversation to approximately 10 KB.
- The stream looked like unreadable/binary data because it was encrypted TLS traffic.
- Following a stream groups conversation data; it does not decrypt TLS.

## Important distinction: `tcp.port == 443` vs `tls`

- `tcp.port == 443` filters by TCP port and can match TCP handshake packets, ACK-only packets, and data segments using port 443.
- `tls` matches packets Wireshark dissects as TLS, including handshake messages and application-data records.
- These filters do not count connections. A single TCP connection can contain many packets, and some port-443 packets may not be dissected as TLS.

Observed counts: `tcp.port == 443` = 72 packets; `tls` = 28 packets.

## Analyst mindset

- Endpoints answer: **which individual hosts appear in the capture?**
- Conversations answer: **which two endpoints communicated, and how much traffic did they exchange?**
- Packets are not the same as connections.
- High packet or byte counts alone do not prove malicious activity.
- A valid filter with zero results is still a useful observation about the capture.

## Next

Finish any final review / active recall, then update roadmap status based on demonstrated understanding.
