# Day 8 — DNS Fundamentals
**Planned date:** 2026-08-31

## Core idea
DNS resolves human-friendly names into IP addresses.

```text
Browser / OS cache
↓
Recursive resolver
↓
Root DNS
↓
TLD DNS
↓
Authoritative DNS
↓
A / AAAA answer
↓
IP address
```

## Important records
- A → IPv4
- AAAA → IPv6
- CNAME → alias
- MX → mail server
- NS → authoritative name server
- TXT → text / verification / policy

## Fedora practical
```bash
dig example.com
dig A example.com
dig MX example.com
dig NS example.com
nslookup example.com
```

## SOC note
A suspicious DNS query is an indicator worth investigating, not automatic proof of malware.