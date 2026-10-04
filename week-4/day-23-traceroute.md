# Day 23 — Traceroute
**Planned date:** 2026-09-15

## Purpose
Traceroute shows responding hops along the path toward a destination.

Understand:
- Hop
- Router
- TTL
- Latency
- Timeout / `*`

## Commands
```bash
traceroute example.com
traceroute 1.1.1.1
```

## Practical result
An `*` does not automatically mean an attack or broken router. A later hop or the destination can still respond.

## Important lesson
`traceroute` can stop showing responses while `ping` and HTTPS still work.