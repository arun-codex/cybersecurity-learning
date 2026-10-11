# 🦈 Day 42 — Mini SOC Wireshark Investigation

**Status: ✅ Complete — controlled lab, practical verification across multiple captures, investigation report, and theory test completed.**

## 🎯 Scenario

Generate repeated failed TCP connection attempts against the learner's own localhost, inspect them in Wireshark, and write an evidence-based assessment rather than immediately labelling the pattern an attack.

## 🧪 Controlled lab

Command used:

```bash
for i in {1..20}; do
    timeout 0.3 bash -c '</dev/tcp/127.0.0.1/9999' 2>/dev/null || true
done
```

- Interface: loopback `lo`
- Display filter: `tcp.port == 9999`
- Destination: `127.0.0.1:9999`

## 🔎 Verified observations

- Total packets captured: 52.
- Packets matching `tcp.port == 9999`: 40.
- Initial SYN packets (`tcp.flags.syn == 1 && tcp.flags.ack == 0`): 20.
- RST packets (`tcp.flags.reset == 1`): 20.
- Source and destination address: `127.0.0.1`.
- The visible attempt series ran from about 0.000000 to 0.089359 seconds on the relative capture timeline.
- Each initial SYN was followed by an `RST, ACK` response.
- The traffic was deliberately generated for this lab.

## 🧠 Evidence-based interpretation

The RST, ACK responses are consistent with local connection refusal because no service was listening on TCP port `9999` at that moment. The pattern would be worth investigating if it appeared unexpectedly on a production endpoint, but repeated connection attempts alone do not prove malicious activity.

## ✅ What is known

- TCP was used.
- Twenty initial connection attempts targeted port 9999.
- Twenty reset responses were captured.
- Both endpoints were localhost.
- The traffic was intentionally generated as a controlled test.

## ❓ What remains unknown

- The PCAP alone does not identify the originating process or its parent.
- The PCAP alone does not establish which user context ran the command.
- The saved capture filename and wall-clock start time were not confirmed during the session.
- The capture does not establish the port's service state outside the test interval.

## 📁 Full investigation report

The requested report with the full sections for scenario, capture, time range, source/destination, protocol/ports, observations, evidence, hypothesis, known/unknown facts, additional evidence and recommendations is available at:

[`investigations/day42-wireshark-investigation.md`](../investigations/day42-wireshark-investigation.md)

## ✅ Definition of done — complete

### Practical evidence checklist
These skills were verified across separate relevant captures; they were not all claimed to come from one PCAP.

- [x] DNS query and response: loopback query for `ab.chatgpt.com`, with a matching response correlated by transaction ID `0xbee3`.
- [x] TCP handshake: SYN → SYN/ACK → ACK in `tcp.stream eq 0`.
- [x] TCP connection/ports: client ephemeral port to server port `443`.
- [x] UDP traffic: UDP packets including DNS and QUIC were visible in the Wi-Fi capture.
- [x] HTTP: local `GET /` to `127.0.0.1:8000` and response `HTTP/1.0 200 OK`.
- [x] TLS handshake: Client Hello with SNI `example.com` and Server Hello identified in a separate capture.
- [x] Source/destination IPs and ports: inspected in TCP, UDP, DNS and HTTP packet details.
- [x] Endpoint and conversation: reviewed in Day 41 Endpoints/Conversations analysis.
- [x] TCP stream: followed `tcp.stream eq 0` in the Day 42 handshake capture and `tcp.stream eq 3` in Day 41 analysis.
- [x] Potentially unusual pattern documented: 20 initial SYNs and 20 RST responses to localhost port `9999`, known to be deliberately generated for this lab.

### Final theory test
- **Score: 7.75/10 — passed.**
- Corrected/reviewed endpoint vs conversation, RST meaning, and the need for corroborating evidence before deciding activity is malicious.

### Key evidence
- Day 41 filter reference: [`wireshark-filters.md`](wireshark-filters.md).
- Day 41 practical notes: [`day-41-filters-streams-endpoints.md`](day-41-filters-streams-endpoints.md).
- Full Day 42 report: [`investigations/day42-wireshark-investigation.md`](../investigations/day42-wireshark-investigation.md).

## TLS handshake evidence (separate Wi-Fi capture)

- `tls.handshake.type == 1` displayed a Client Hello with SNI `example.com`.
- `tls.handshake.type == 2` displayed a Server Hello (packet 27 in that capture).
- Server source port: `443`; client destination port: `46608`.
- This was a separate 56-packet capture, not the localhost port-9999 PCAP.

## ➡️ Next

**Day 43 — Nmap + network enumeration (Week 7).**
