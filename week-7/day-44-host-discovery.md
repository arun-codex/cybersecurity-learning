# Day 44 — Host Discovery + Target Scope

**Status:** Complete with guided active-recall correction.  
**Evidence timestamp:** Terminal output dated 2026-10-13, 21:23 IST.  
**Environment:** Fedora Linux; Nmap 7.92.  
**Target/scope:** Own machine only; loopback target `127.0.0.1`.

## Objective

Distinguish host discovery from port scanning, inspect local interface/routing information, use `-sn` against an authorized target, and record what the result does and does not prove.

## Commands and observed results

### 1. Inspect addresses

Commands used:

```bash
ip addr
ip -br address
```

Observed:
- Loopback interface `lo` was up and had `127.0.0.1/8` and `::1/128`.
- A Wi-Fi interface was up and had a dynamically assigned IPv4 address and IPv6 addresses.
- The Ethernet interface showed `NO-CARRIER` and `state DOWN`.
- This public note deliberately omits the machine's private/local IP addresses, MAC address and specific gateway details because they are unnecessary to demonstrate the host-discovery result.

### 2. Inspect routing

Command:

```bash
ip route
```

Observed:
- A default route existed through the local gateway over the Wi-Fi interface.
- A directly connected IPv4 route existed for the local `/24` network.
- Exact local addressing and gateway details are intentionally omitted from this public note.

### 3. Host discovery only

Command:

```bash
nmap -sn 127.0.0.1
```

Actual output:

```text
Starting Nmap 7.92 ( https://nmap.org ) at 2026-10-13 21:23 IST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds
```

## Findings

### Observation

Nmap reported the local loopback host `127.0.0.1` as up in this discovery run. The command used `-sn`, so the output contained no normal port table.

### Interpretation

- `-sn` requests host discovery without a normal port scan.
- `nmap 127.0.0.1` (without `-sn`) normally performs host discovery and then a default TCP port scan when the target is considered up.
- A positive response supports that the target was responsive to the discovery process at that time.
- No response would not, on its own, prove that a host is offline. Firewalls, network paths, and probe behavior can affect the outcome.
- Confirm the target address and authorization before any scan; an incorrect address can lead to testing the wrong system.
- This localhost result does not discover or inventory other devices on the Wi-Fi network. No subnet or arbitrary public IP range was scanned.

## Active recall and review

Completed after guided correction:
- Identified `-sn` as host discovery without a normal port scan.
- Confirmed that host discovery alone does not enumerate all open ports.
- Identified firewalls as one reason for no response and learned that no response is inconclusive.
- Identified target verification as a way to ensure the intended, authorized system is being checked.
- Distinguished an observed responsive host from an assumed host.

**Review point:** The `-sn` vs. normal scan distinction initially needed additional prompting. Revisit this without notes before the next assessment.

## Day 44 checklist

- [x] Explain the purpose of host discovery
- [x] Use `-sn` against an authorized target (localhost)
- [x] Understand that no response does not conclusively prove a host is offline
- [x] Record actual command and result, including limitations
- [x] Complete active recall with guided correction

## Next

**Day 45 — Port states: open, closed and filtered.** Use a controlled local lab and correlate Nmap observations with actual local service/listener state. Do not scan targets without authorization.
