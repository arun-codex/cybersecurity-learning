# Day 25 — Connection Inspection with ss
**Planned date:** 2026-09-17

## Commands
```bash
sudo ss -tnp
sudo ss -lntp | grep ':22'
```

## Observed
Firefox, Spotify and GNOME Software had active network connections. Several remote services used port 443.

The SSH listener check returned no matching listener on port 22.

## SOC distinction
```text
Firewall rule → traffic permitted
LISTEN → service waiting
ESTABLISHED → connection exists
``` 