# Day 24 — Firewall + Fedora firewalld
**Planned date:** 2026-09-16

## Concepts
ALLOW · DENY · REJECT · RULE · PORT · SERVICE · DEFAULT POLICY · ZONE

## Fedora practical
```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --list-all
sudo firewall-cmd --list-services
sudo firewall-cmd --list-ports
```

## Observed configuration
- Active zone: FedoraWorkstation
- Interface: wlp0s20f3
- Services: dhcpv6-client, samba-client, ssh
- Ports: 1025-65535/tcp and 1025-65535/udp

## Security lesson
Firewall configuration ≠ active traffic.