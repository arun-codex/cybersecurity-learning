# Day 43 — Nmap + First Localhost Scan

**Status:** Complete — practical commands, TCP/UDP socket comparison and guided active recall completed.  
**Evidence timestamp:** Terminal output dated 2026-10-12, 06:26–06:36 IST.  
**Environment:** Fedora Linux 44; Nmap 7.92.  
**Target/scope:** Own machine only, using loopback target `127.0.0.1`.

## Goal

Check Nmap availability, run a first localhost scan, scan selected TCP ports, compare observations with local socket information, and separate verified facts from possible explanations.

## Commands and actual results

### 1. Check Nmap

Command:

```bash
nmap --version
```

Observed: `Nmap version 7.92`, platform `x86_64-redhat-linux-gnu`.

The install check `sudo dnf install nmap` reported that `nmap-4:7.92-11.fc44.x86_64` was already installed; no installation was needed.

### 2. First localhost scan — 06:26 IST

Command:

```bash
nmap 127.0.0.1
```

Observed output:

```text
Host is up (0.00052s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
631/tcp  open  ipp
8000/tcp open  http-alt
```

Nmap reported one host up and completed the scan in 0.14 seconds.

### 3. Targeted TCP scan — 06:36 IST

Command:

```bash
nmap -p 22,80,443,8000,9999 127.0.0.1
```

Observed states:

```text
PORT     STATE  SERVICE
22/tcp   closed ssh
80/tcp   closed http
443/tcp  closed https
8000/tcp closed http-alt
9999/tcp closed abyss
```

### 4. Repeated full scan — 06:36 IST

Command:

```bash
nmap 127.0.0.1
```

Observed:

```text
Host is up (0.00018s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT    STATE SERVICE
631/tcp open  ipp
```

This later full scan showed port 631 open while port 8000 was no longer listed as open.

### 5. Compare local socket information

Commands:

```bash
ss -lnt
ss -lnu
```

The TCP output included:

```text
LISTEN ... 127.0.0.1:631 ...
LISTEN ... [::1]:631 ...
```

No TCP listener for port 8000 appeared in the provided `ss -lnt` output.

The UDP output showed local UDP sockets, including entries on ports 5353 and 5355 and the local stub resolver addresses on port 53. This is not a direct comparison with the Nmap scans above, which tested TCP ports.

## Findings: observation vs. interpretation

### Observed facts

- The initial scan showed `631/tcp` and `8000/tcp` open.
- The later targeted scan showed all five selected ports — 22, 80, 443, 8000 and 9999 — closed.
- The later full scan showed `631/tcp` open.
- `ss -lnt` showed TCP listeners at `127.0.0.1:631` and `[::1]:631`.
- The later socket listing did not show a listener on TCP port 8000.

### Interpretation and limits

- **Port 631:** Nmap's open result and the local `LISTEN` entries support the conclusion that a TCP service was listening on port 631 at the time of the later checks. The Nmap label `ipp` is a conventional port/service label; these results alone do not independently identify the application.
- **Port 8000:** The observed state changed from open to closed between scans. The later `ss` output is consistent with no listener on that port then, but the cause of the change was not established.
- **Closed ports:** Nmap reported connection refusal for the closed TCP ports shown in the full scan. Interpret scan results as observations at a particular time, not as permanent system properties.
- **TCP vs. UDP:** `ss -lnt` lists local TCP listening sockets; `ss -lnu` lists local UDP sockets. A TCP scan should be compared with TCP socket evidence, not treated as directly verified by a UDP listing.
- Labels such as `http-alt` and `ipp` do not, by themselves, confirm which application is running.

## Active recall

After guided correction, the key answers were:

1. Port 631: `LISTEN` means a TCP socket is waiting for incoming connections; Nmap and `ss` findings agree.
2. Port 8000: its observed state changed; the cause remains unknown.
3. TCP vs. UDP: the Nmap commands checked TCP ports while `ss -lnu` displays local UDP sockets.

**Reflection:** The concepts were answered correctly after guided explanation. Revisit the distinctions between a scan result and a local socket listing, plus observation vs. inference, in later reviews.

## Day 43 completion checklist

- [x] Verify Nmap version and installation
- [x] Run `nmap 127.0.0.1`
- [x] Scan selected TCP ports
- [x] Compare results with `ss -lnt` and inspect `ss -lnu`
- [x] Record actual evidence and acknowledge unknown cause for port 8000
- [x] Complete active recall with guided correction

## Next

**Day 44 — Host discovery and authorized target scope.** Start with the planned localhost discovery exercise and inspect local addresses/routes. Do not scan random networks.
