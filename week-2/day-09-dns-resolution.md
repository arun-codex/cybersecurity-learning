# Day 9 — DNS Resolution + Troubleshooting
**Planned date:** 2026-09-01

## Resolution flow
Browser → OS/local cache → recursive resolver → root → TLD → authoritative server → IP.

## Practical
```bash
dig example.com
dig +short example.com
dig google.com
```

Observe:
- IP addresses
- TTL
- Query time
- DNS server
- Answer section
- Status

## SOC rule
If a suspicious domain is queried, investigate supporting evidence before concluding compromise.