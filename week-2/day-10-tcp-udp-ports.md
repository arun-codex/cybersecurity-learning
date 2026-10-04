# Day 10 — TCP vs UDP + Ports
**Planned date:** 2026-09-02

## TCP
- Connection-oriented
- Reliable delivery mechanisms
- Ordered delivery
- ACKs / retransmissions
- Three-way handshake

## UDP
- Connectionless
- No TCP-style handshake
- Lower overhead
- No TCP-style delivery guarantee
- No TCP-style ordering

## Three-way handshake
```text
Client → SYN → Server
Client ← SYN-ACK ← Server
Client → ACK → Server
```

## Ports
21 FTP · 22 SSH · 23 Telnet · 25 SMTP · 53 DNS · 80 HTTP · 443 HTTPS