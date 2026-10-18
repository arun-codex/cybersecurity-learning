# Day 46 — Basic Scans, Service Detection + Saved Output

**Status:** Complete with guided active-recall review.  
**Evidence timestamps:** Terminal outputs dated 2026-10-18, 23:02–23:32 IST.  
**Environment:** Fedora Linux; Nmap 7.92; Python 3.14.8.  
**Target/scope:** Own machine only; loopback target `127.0.0.1`.

## Objective

Compare a basic scan with service/version detection, corroborate the listening socket using `ss`, and save readable Nmap output.

## 1. Start a local HTTP server

Command in Terminal 1:

```bash
cd ~/cyber-lab/week7
python3 -m http.server 8000 --bind 127.0.0.1
```

Actual startup message:

```text
Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...
```

The server was bound to loopback for this local lab.

## 2. Scan two selected TCP ports — 23:02 IST

Command:

```bash
nmap -p 8000,9999 127.0.0.1
```

Actual relevant output:

```text
PORT     STATE  SERVICE
8000/tcp open   http-alt
9999/tcp closed abyss
```

Observation:
- TCP/8000 was reported open while the test server was running.
- TCP/9999 was reported closed.
- `http-alt` and `abyss` are Nmap service-name labels, not conclusive application identification.

## 3. Service/version detection — 23:04 IST

Command:

```bash
nmap -sV -p 8000 127.0.0.1
```

Actual relevant output:

```text
PORT     STATE SERVICE VERSION
8000/tcp open  http    SimpleHTTPServer 0.6 (Python 3.14.8)
```

Nmap identified HTTP and reported `SimpleHTTPServer 0.6 (Python 3.14.8)`. Compared with the basic scan's port-based label, `-sV` sent additional probes and produced more specific service information. This run took 7.19 seconds.

## 4. Save normal output — 23:32 IST

Command:

```bash
nmap -sV -p 8000 127.0.0.1 -oN ~/cyber-lab/week7/day46-service-detection.txt
```

The scan reported the same service identification and took 6.46 seconds.

Inspected the actual file:

```bash
cat ~/cyber-lab/week7/day46-service-detection.txt
```

The file contained:
- Nmap version and command used
- Scan date/time
- Target and host status
- Port state, service and version information
- Scan completion time and duration

**Local artifact:** `~/cyber-lab/week7/day46-service-detection.txt`. The saved output is on the Fedora machine; this note records the result in the GitHub learning repository.

## 5. Compare against local socket information

Command:

```bash
ss -lnt '( sport = :8000 )'
```

Actual relevant output:

```text
State  Recv-Q Send-Q Local Address:Port Peer Address:Port
LISTEN 0      5          127.0.0.1:8000      0.0.0.0:*
```

Interpretation:
- Nmap observed TCP/8000 as open and identified the HTTP service.
- `ss` reported a local TCP listening socket bound to `127.0.0.1:8000`.
- These observations agree that the local test server was listening at the time of the checks.
- Nmap and `ss` have different roles: Nmap probes and interprets responses; `ss` shows local socket information.

## 6. Active recall review

Completed with guidance:
- `-sV` adds service and possible version identification.
- `ss` shows local listening-socket information; Nmap reports scan observations and can identify the service with `-sV`.
- `-oN` saves readable normal output, which can be reviewed later and used as investigation evidence.
- A basic service label based on a port number does not prove the exact application because services can use nonstandard ports.
- Applications can use nonstandard ports due to configuration, multiple instances, development/testing, or other setup choices; a busy standard port is one possible but not universal explanation.
- The Python HTTP server was stopped with `Ctrl+C` at the end of the lab.

**Review note:** Answers were correct after guided prompting. Revisit the purpose of `-sV`, why port labels are not proof, and the difference between Nmap and `ss` during the next closed-notes review.

## Day 46 checklist

- [x] Run a small, scoped scan
- [x] Perform service/version detection on the local test server
- [x] Compare basic scan and `-sV` results
- [x] Save and inspect readable Nmap output
- [x] Compare the scan with a local listening-socket check
- [x] Stop the temporary HTTP server
- [x] Complete active recall with guided correction

## Next

**Day 47 — Light review: ports, services and TCP states.** Recall first without notes, compare Nmap with `ss`, and record one difference or uncertainty.
