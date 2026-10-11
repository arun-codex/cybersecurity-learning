# 🦈 Day 41 — Wireshark Filters, Streams, Endpoints

**Status: ✅ Complete — practical filtering, stream inspection, endpoint/conversation analysis and active recall passed.**

## 🎯 Goal

Reduce packet-capture noise and move from individual packets to host and connection-level understanding.

## 📁 Capture

- Capture used: `day36-basic-capture.pcapng`
- Total packets: 97

## 🔎 Filters practiced

| Filter | Result | What it showed |
|---|---:|---|
| `dns` | 2 | Query and response for `example.com`, type AAAA |
| `ip.dst == 192.168.1.9` | 3 | IPv4 packets arriving at the host |
| `ip.src == 192.168.1.9` | 5 | IPv4 packets from the host |
| `ip.addr == 192.168.1.9` | 8 | IPv4 packets in either direction |
| `tcp.port == 443` | 72 | TCP packets using port 443 |
| `udp.port == 53` | 2 | UDP DNS query and response |
| `tcp.flags.syn == 1` | 2 | Initial SYN and SYN/ACK |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | 1 | Initial SYN in this capture |
| `tcp.flags.reset == 1` | 0 | No TCP resets matched |
| `tcp.analysis.retransmission` | 0 | No retransmissions identified |
| `tcp.analysis.duplicate_ack` | 0 | No duplicate ACKs identified |
| `tls` | 28 | Packets Wireshark dissected as TLS |

Zero matches apply only to this 97-packet capture; they do not prove such events never happen.

## 🔗 Follow TCP Stream

Followed `tcp.stream eq 3`.

- Wireshark reassembled approximately 10 KB of conversation data.
- The content looked binary/unreadable because it was encrypted TLS traffic.
- Following a stream groups data from a TCP conversation; it does not decrypt TLS.

## 📊 Endpoints

### IPv4
- `192.168.1.9`: 8 packets, approximately 1 KB; 5 transmitted packets / 566 bytes and 3 received / 462 bytes.
- `192.168.1.4`: 6 packets / 836 bytes.
- `192.168.1.1`: 2 packets / 192 bytes.

The busiest endpoint in the displayed IPv4 tab was `192.168.1.9`.

### IPv6
- Highest packet count shown: `2401:4900:88b4:91a:d6fe:fa54:f22b:c5a5`
- 89 packets / approximately 46 KB; 42 transmitted / 30 KB and 47 received / 16 KB.

Check both IPv4 and IPv6 before deciding which endpoint is busiest overall.

## 💬 Conversations

### TCP
The table showed 9 TCP conversations.

- Most packets: 25 packets / 11 KB, stream ID 6, client port `50756` to server port `443`.
- Most bytes: 17 KB / 20 packets, stream ID 4, client port `36890` to server port `443`.

The conversation with the most packets was not the conversation with the most bytes.

### UDP / DNS
- Client: `192.168.1.9:48606`
- DNS server: `192.168.1.1:53`
- 2 packets / 192 bytes
- Client → server: 1 packet / 82 bytes
- Server → client: 1 packet / 110 bytes
- Duration: approximately 0.048 seconds
- Query type: AAAA for `example.com`

## 🧠 Key distinction

- `tcp.port == 443` matches TCP packets based on port, including handshake, ACK and data packets.
- `tls` matches packets Wireshark dissects as TLS, including handshake messages and application-data records.
- Packet count is not connection count.
- High traffic volume or a zero-result filter alone does not establish maliciousness.

## ✅ Active recall passed

Confirmed that the `tls` filter can show TLS handshake packets (such as Client Hello and Server Hello) as well as application-data packets.

## 📚 Detailed notes

See [`notes/day41-filters.md`](../notes/day41-filters.md) for the Top 10 filter reference and the full set of observed results.

## ➡️ Next

**Day 42 — Mini SOC Wireshark Investigation.**
