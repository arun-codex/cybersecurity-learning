# Day 18 — Linux Permissions + Users + Groups
**Planned date:** 2026-09-10

## Permissions
```text
r = 4
w = 2
x = 1

7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---
```

## Example
`chmod 755 script.sh`
- Owner = rwx
- Group = r-x
- Others = r-x

## Practical
```bash
touch permission-test.txt
ls -l permission-test.txt
chmod 600 permission-test.txt
chmod 644 permission-test.txt
whoami
id
```

## SOC connection
Unexpected ownership, permissions or executable files may become investigation evidence.