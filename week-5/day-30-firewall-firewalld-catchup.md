# Day 30 — Week 4 Catch-up: Firewall + firewalld
**Planned date:** 2026-09-22

## Fedora inspection
```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --list-all
sudo firewall-cmd --list-services
sudo firewall-cmd --list-ports
```

## Actual configuration observed
- Zone: FedoraWorkstation
- Interface: wlp0s20f3
- Services: dhcpv6-client, samba-client, ssh
- Ports: 1025-65535/tcp and 1025-65535/udp

## Connection evidence
```bash
sudo ss -tnp
sudo ss -lntp | grep ':22'
```

The SSH listener check returned no matching listener.

## Key lesson
Firewall rule ≠ active connection.