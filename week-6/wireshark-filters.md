# ⭐ Wireshark Filters — Quick Reference

Use these as **display filters** in Wireshark. Display filters change which packets are visible; they do not remove packets from the capture.

## Top 10

| # | Display filter | Use |
|---:|---|---|
| 1 | `dns` | DNS packets |
| 2 | `tcp` | TCP packets |
| 3 | `udp` | UDP packets |
| 4 | `http` | Packets dissected as HTTP |
| 5 | `tls` | Packets dissected as TLS, including handshakes and application data |
| 6 | `ip.addr == 192.168.1.9` | IPv4 traffic to or from this host |
| 7 | `tcp.port == 443` | TCP traffic where source or destination port is 443 |
| 8 | `udp.port == 53` | UDP traffic where source or destination port is 53 |
| 9 | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Initial TCP SYN packets |
| 10 | `tcp.analysis.retransmission` | Retransmissions identified by Wireshark |

## More useful filters

```text
ip.src == 192.168.1.9
ip.dst == 192.168.1.9
ip.addr == 1.1.1.1
ip.src == 192.168.1.9 && tcp.port == 443
tcp.flags.syn == 1
tcp.flags.reset == 1
tcp.analysis.duplicate_ack
udp.port == 53
tls.handshake.type == 1
tls.handshake.type == 2
tcp.stream eq 3
tcp.port == 9999
```

## Capture filter vs display filter

- **Capture filter:** limits which packets get recorded during capture; uses capture-filter syntax (BPF/libpcap).
- **Display filter:** filters the packets shown after capture; uses Wireshark display-filter syntax.

## Reading results carefully

- `tcp.port == 443` selects by TCP port; `tls` selects packets Wireshark recognizes as TLS. Their counts can differ.
- Packet counts are not connection counts.
- `tcp.flags.reset == 1` is the reset-flag field used in the learner's Wireshark version.
- `ip.*` filters are for IPv4 and do not match IPv6 packets. Use `ipv6.addr`, `ipv6.src`, or `ipv6.dst` for IPv6.
- Zero results mean no packets matched in that capture; they do not prove the event never happened.
- Port 443 commonly carries HTTPS/TLS, but a port number alone does not prove the application protocol.

## Related lab notes

- [Day 41 — Filters, Streams and Endpoints](day-41-filters-streams-endpoints.md)
- [Day 42 — Mini SOC Investigation](day-42-wireshark-investigation.md)
