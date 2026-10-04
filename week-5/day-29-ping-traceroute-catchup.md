# Day 29 — Week 4 Catch-up: Ping + Traceroute
**Planned date:** 2026-09-21

## Recall
- ICMP
- ping
- latency
- packet loss
- traceroute
- TTL
- hops
- `*` responses

## Practical
```bash
ping -c 4 google.com
ping -c 4 1.1.1.1
ping -c 4 example.com
traceroute google.com
traceroute 1.1.1.1
```

## SOC reasoning
A known IP working while a domain fails can indicate a DNS-related problem. Do not immediately call unusual network behavior an attack.