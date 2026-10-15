# Day 45 — Port States + TCP Connection Reasoning

**Status:** In progress — controlled local scans completed; evidence-vs-inference write-up and final active recall remain.  
**Evidence timestamp:** Terminal output dated 2026-10-15, 23:24–23:26 IST.  
**Environment:** Fedora Linux; Nmap 7.92.  
**Target/scope:** Own machine only, loopback target `127.0.0.1`.

## Objective

Compare a port with a listening local HTTP test service against a port with no listener, then observe port 8000 after stopping the test server. Practise interpreting Nmap's states without assuming that an open port is automatically vulnerable.

## Commands and actual scan results

### 1. Port 8000 during the server-running phase — 23:24 IST

Command:

```bash
nmap -p 8000 127.0.0.1
```

Observed output:

```text
PORT     STATE SERVICE
8000/tcp open  http-alt
```

Observation: Nmap reported TCP/8000 as open.

### 2. Port 9999 — 23:25 IST

Command:

```bash
nmap -p 9999 127.0.0.1
```

Observed output:

```text
PORT     STATE  SERVICE
9999/tcp closed abyss
```

Observation: Nmap reported TCP/9999 as closed.

### 3. Port 8000 after stopping the test server — 23:26 IST

Command:

```bash
nmap -p 8000 127.0.0.1
```

Observed output:

```text
PORT     STATE  SERVICE
8000/tcp closed http-alt
```

Observation: Nmap reported TCP/8000 as closed after the server was stopped.

Service strings such as `http-alt` and `abyss` are Nmap's service-name labels; they do not independently establish the exact application.

## Findings: evidence vs. inference

### Observations

- TCP/8000 was reported `open` at 23:24 IST.
- TCP/9999 was reported `closed` at 23:25 IST.
- TCP/8000 was reported `closed` at 23:26 IST, after the test server was stopped.

### Supported interpretation

- During the server-running phase, Nmap's `open` result was consistent with a service accepting TCP connections on port 8000.
- A `closed` result means the target responded, but no application appeared to be listening on that TCP port at scan time.
- The before/after results are consistent with the local test service listening on port 8000 while running and no longer listening after it stopped.

### What is not proven

- An open port alone does not prove the service is vulnerable or that the computer is compromised.
- The service label alone does not confirm the precise application or version.
- These scans did not demonstrate the `filtered` state; do not classify a port as filtered without supporting scan evidence.
- A result describes Nmap's view from this scan location and time; a scan from another network path may see a different state.

### Additional verification

A local listener check can corroborate the Nmap result:

```bash
ss -lnt
```

To check only TCP/8000 more directly, use:

```bash
ss -lnt '( sport = :8000 )'
```

These checks inspect local TCP listening sockets; they supplement rather than replace the Nmap observation.

## Core interpretation table

| State | Basic meaning |
|---|---|
| `open` | A service appears to accept connections or traffic on the port. |
| `closed` | The target responds, but no application appears to be listening on the port. |
| `filtered` | Nmap cannot determine whether the port is open because filtering or another network obstacle prevents a clear result. |

TCP connection reasoning reminder: SYN → SYN/ACK → ACK establishes a normal TCP connection. A RST can indicate rejection or reset depending on context; it is different from an orderly FIN-based shutdown.

## Day 45 checklist

- [x] Test an open local port during the server-running phase
- [x] Compare it with a port reported closed
- [x] Stop the test server and observe TCP/8000 become closed
- [ ] Independently explain all three primary states without notes
- [ ] Complete the evidence-vs-inference write-up and final active recall

## Next

Finish the active-recall questions and evidence-vs-inference exercise, then update the completion status. Day 46 follows only after Day 45 review is complete.
