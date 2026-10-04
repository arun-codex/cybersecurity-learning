# Day 5 — IPv4 Addressing + Subnetting
**Planned date:** 2026-08-28

## Key ideas
- An IP address identifies a network interface/destination.
- A subnet mask separates network and host portions.
- Private IP space is used inside private networks.

## Notes from practice
```text
255.255.255.0  → 254 usable hosts
255.255.255.248 → 6 usable hosts
```

**Correction:** `255.255.255.250` is not a valid normal subnet mask because mask bits must be contiguous.