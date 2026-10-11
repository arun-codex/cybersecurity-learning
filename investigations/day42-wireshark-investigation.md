# 🦈 Week 6 Wireshark Investigation

## 🎯 Scenario

A controlled local test generated 20 TCP connection attempts to `127.0.0.1:9999` using Bash's `/dev/tcp` feature wrapped with `timeout`. The test was intentionally run by the learner against their own machine; it is a benign lab, not evidence of an external attack.

Command used:

```bash
for i in {1..20}; do
    timeout 0.3 bash -c '</dev/tcp/127.0.0.1/9999' 2>/dev/null || true
done
```

Capture interface: loopback `lo`.
Display filter: `tcp.port == 9999`.

## 📁 Capture File

The screenshot shows a 52-packet capture, but the saved PCAP filename was not confirmed in the session. If not already saved, save the capture as `day42-localhost-9999.pcapng`.

## ⏱️ Time Range

The visible relative packet timestamps run from approximately `0.000000` seconds to `0.089359` seconds for the observed attempt series. This is a relative capture timeline, not a verified wall-clock incident time.

## 🌐 Source

`127.0.0.1` (IPv4 loopback / localhost).

The displayed initial SYN packets used varying ephemeral source ports, including `40982`, `41006`, `41014`, and others.

## 🌐 Destination

`127.0.0.1` (the same local machine).

## 🔌 Protocol

TCP.

## 🔢 Ports

- Destination service port for the attempts: `9999`.
- Client source ports: varying ephemeral ports.
- Reset responses: source port `9999` to each client's ephemeral port.

## 👀 Observations

- Total packets in the capture: **52**.
- Packets displayed by `tcp.port == 9999`: **40**.
- Initial SYN packets (`tcp.flags.syn == 1 && tcp.flags.ack == 0`): **20**.
- TCP reset packets (`tcp.flags.reset == 1`): **20**.
- The packet list shows each initial SYN followed by a corresponding `RST, ACK` response.
- The sequence occurred rapidly, within approximately 0.09 seconds in the visible relative timeline.
- Both source and destination IP addresses were `127.0.0.1`.

## 🔎 Evidence

1. The display filter `tcp.port == 9999` showed 40 packets.
2. The initial-SYN filter showed 20 packets.
3. The reset filter `tcp.flags.reset == 1` showed 20 packets.
4. Packet details and the Info column showed client ephemeral ports sending `SYN` to port `9999`.
5. The corresponding replies originated from port `9999` and were labelled `RST, ACK`.
6. The traffic was generated intentionally with a local test command on `lo`.

## 🚨 Suspicious Indicators

If the same pattern appeared unexpectedly in a production host, repeated connection attempts to one port over a short interval could merit investigation. Here, the pattern is expected because it was deliberately generated as a lab exercise.

Repeated attempts alone do not establish malicious activity.

## 🧠 Hypothesis

The connection attempts were refused/reset because no service was listening on local TCP port `9999` at the time of the test. The observed `RST, ACK` replies are consistent with that explanation.

This is an evidence-based interpretation of the capture, not proof about every possible service state outside the capture interval.

## ✅ What We Know

- The source and destination were both `127.0.0.1`.
- TCP was used.
- Twenty initial SYN packets targeted port `9999`.
- Twenty RST packets were observed as responses.
- The events occurred within a very short interval.
- The learner intentionally generated the traffic for a controlled lab.

## ❓ What We Don't Know

- The capture alone does not identify the originating process or parent process.
- The capture alone does not establish which user context executed the command.
- The capture does not prove the port's listening state outside the observed time.
- The saved PCAP filename and wall-clock start time were not confirmed in the session.

## 🔍 Additional Evidence Needed

For a real, unexpected occurrence, collect and correlate:
- Process and parent-process details from endpoint telemetry.
- User/device context and shell or process logs.
- Listening sockets and services at the relevant time (for example, `ss -lntp`).
- Host logs and the precise time range.
- Related connections to other ports or destinations.
- DNS history if hostnames are involved; this test used a direct loopback IP, so DNS was not required.

## 🧪 Practical checklist and theory assessment

Practical verification was completed across several relevant captures rather than one capture:
- DNS query/response in a loopback capture; query/response correlation used transaction ID `0xbee3`.
- TCP handshake confirmed in stream 0: SYN, SYN/ACK, ACK.
- UDP traffic observed, including DNS and QUIC in the Wi-Fi capture.
- Local HTTP request to `127.0.0.1:8000` and `HTTP/1.0 200 OK` response.
- TLS Client Hello with SNI `example.com` and Server Hello identified in a separate Wi-Fi capture.
- Endpoints, Conversations and Follow TCP Stream were practiced and documented previously in Day 41.
- Source/destination addresses, ports and one controlled repeated-connection pattern were identified.

Theory test score: **7.75/10 — passed**. Endpoint vs conversation terminology and the interpretation of RST were corrected/reviewed.

## 📝 Conclusion

The capture contains 20 TCP connection attempts to `127.0.0.1:9999` and 20 corresponding `RST, ACK` responses. The pattern is consistent with repeated attempts to reach a local port with no listening service. Since the traffic was intentionally generated by the learner in a controlled localhost exercise, it is benign test traffic. The same packet pattern in another context would warrant correlation with process, host, user, and timing evidence before drawing a conclusion.

## 🛡️ Recommended Next Steps

1. Save the capture with a descriptive filename if it has not already been saved.
2. Keep the raw PCAP alongside this report when practical.
3. In real investigations, establish process/user attribution and correlate the event with host logs.
4. Continue with Day 43 — Nmap + network enumeration (Week 7).
