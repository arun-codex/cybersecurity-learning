# Day 19 — Processes + Services
**Planned date:** 2026-09-11

## Processes
A process is a running instance of a program.

```bash
ps
ps aux
top
ps aux | grep firefox
ps aux | grep ssh
```

Observe:
- PID
- USER
- CPU
- Memory
- Process name

## Services
```bash
systemctl status NetworkManager
systemctl --type=service --state=running
```

## SOC questions
What is running? Who owns it? Is it expected?