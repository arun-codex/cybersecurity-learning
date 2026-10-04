# Day 17 — grep + find + Log Investigation
**Planned date:** 2026-09-09

## grep
```bash
grep "error" logs.txt
grep -i "error" logs.txt
grep -n "error" logs.txt
```

## find
```bash
find . -name "*.txt"
find . -type d
find . -type f
```

## SOC use
```text
Raw Logs → Search → Interesting Events → Investigation
```

## Key idea
Text-searching is a practical way to reduce thousands of log lines to relevant events.