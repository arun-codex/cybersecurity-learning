# Day 35 — Week 5 Integration + Mini SOC Investigation
**Planned date:** 2026-09-27

## Status
**Next / pending**

## Scenario
```text
2026-09-26 22:01 Failed login user=admin src=192.168.1.50
2026-09-26 22:02 Failed login user=admin src=192.168.1.50
2026-09-26 22:03 Failed login user=admin src=192.168.1.50
2026-09-26 22:04 Failed login user=admin src=192.168.1.50
2026-09-26 22:05 Successful login user=admin src=192.168.1.50
2026-09-26 22:06 File accessed=/home/admin/passwords.txt
2026-09-26 22:07 Connection to 203.0.113.50
```

## Investigation commands
```bash
cat security-events.log
grep "Failed" security-events.log
grep "Successful" security-events.log
grep "admin" security-events.log
grep -n "203.0.113.50" security-events.log
```

## Questions
1. What happened?
2. What is suspicious?
3. What is the possible IOC?
4. Is this proof of compromise?
5. What would you investigate next?

## MITRE thinking
Observed behavior → repeated failed logins → possible authentication attack → potential credential access.

Do not force a mapping when evidence is insufficient.