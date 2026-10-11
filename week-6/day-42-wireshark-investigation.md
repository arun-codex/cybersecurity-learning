# 🦈 Day 42 — Mini SOC Wireshark Investigation

**Status: 🟡 In progress — controlled lab and report drafted; final theory test and remaining practical checklist pending.**

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

## 📝 Remaining definition of done

- [ ] Complete the 10-question theory test without notes.
- [ ] Confirm practical evidence in a capture: DNS query/response, TCP handshake/connection, UDP, HTTP, TLS handshake, IPs, ports, endpoint, conversation and TCP stream.
- [ ] Identify and document one potentially unusual pattern from a capture.
- [ ] Complete active recall and review before marking Day 42 complete.

## ➡️ Next

Resume with the Day 42 theory test, then complete any practical evidence items not yet demonstrated.
