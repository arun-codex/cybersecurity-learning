# Day 13 — Browser-to-Server Traffic Flow
**Planned date:** 2026-09-05

## Full flow
```text
Browser
↓
DNS
↓
IP
↓
TCP connection
↓
TLS
↓
HTTPS request
↓
Server
↓
HTTPS response
↓
Browser
```

## Practical
```bash
dig example.com
ping example.com
traceroute example.com
curl -I https://example.com
curl -v https://example.com
```

## SOC questions
Who communicated? With whom? Which protocol? Which port? What was requested? What response occurred? Is anything unusual?