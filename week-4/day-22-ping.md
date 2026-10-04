# Day 22 — Ping + Connectivity
**Planned date:** 2026-09-14

## What ping tests
`ping` uses ICMP Echo Requests/Replies.

It helps observe:
- Basic connectivity
- Latency
- Packet loss
- Timeouts

## Practical
```bash
ping -c 4 example.com
ping -c 4 google.com
ping -c 4 1.1.1.1
```

## Troubleshooting
If `1.1.1.1` works but `example.com` fails, investigate DNS/name resolution first.

## Important
Ping success does not prove that every service/application is working.