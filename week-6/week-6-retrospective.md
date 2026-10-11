# 🧭 Week 6 Retrospective — Me vs. Me

**Week:** 6 — Wireshark / Packet Analysis  
**Status:** ✅ Complete  
**Next:** Week 7 — Nmap + Network Enumeration  
**Purpose:** Keep progress evidence-based. This review measures my work against my own goals, not against other learners.

---

## ✅ Week 6 definition of done

The Week 6 main goal was to move from asking “What button does Wireshark have?” to asking “What happened?” Evidence was collected across multiple relevant captures, not all from one single PCAP.

- [x] Capture my own traffic and navigate Packet List, Packet Details and packet bytes.
- [x] Identify Ethernet/IP details, including source/destination addressing and protocol information.
- [x] Identify TCP and UDP traffic, ports and direction.
- [x] Recognize the TCP three-way handshake: SYN → SYN/ACK → ACK.
- [x] Inspect TCP data and normal connection termination.
- [x] Identify DNS queries/responses and correlate them using transaction IDs.
- [x] Inspect a readable HTTP request and response in a local lab.
- [x] Recognize TLS Client Hello, Server Hello and encrypted application traffic.
- [x] Use protocol, IP, port, TCP flag, retransmission, duplicate-ACK and TLS display filters.
- [x] Follow a TCP stream.
- [x] Review Endpoints and Conversations statistics.
- [x] Identify an unusual-looking pattern and investigate it without automatically calling it malicious.
- [x] Separate observed facts from hypotheses and unknowns.
- [x] Write a SOC-style investigation report and document progress on GitHub.

## 📅 Day-by-day completion

| Day | Status | Evidence / output |
|---|---|---|
| Day 36 — Wireshark basics | ✅ Complete | Captured traffic and inspected DNS, ICMP, TCP and TLS packets. |
| Day 37 — Ethernet + IP | ✅ Complete | Inspected Ethernet/IP fields, addressing, protocol and ICMP traffic. |
| Day 38 — TCP + UDP | ✅ Complete | Identified SYN/SYN-ACK/ACK, TCP data/FIN, and UDP DNS query/response. |
| Day 39 — DNS + HTTP | ✅ Complete | Correlated DNS query/response; used a local HTTP server and inspected GET and 200 OK. |
| Day 40 — TLS + HTTPS | ✅ Complete | Identified Client Hello/SNI, Server Hello, TLS negotiation and encrypted application data; completed SOC evidence recall. |
| Day 41 — Filters, streams, endpoints | ✅ Complete | Tested filters, followed streams, and used Endpoints/Conversations. Active recall passed. |
| Day 42 — Mini SOC investigation | ✅ Complete | Generated 20 local TCP attempts; verified 20 initial SYNs and 20 RST responses; theory test 7.75/10. |

### Day 42 controlled-lab evidence

- Interface: loopback `lo`
- Target: `127.0.0.1:9999`
- Total capture: 52 packets
- `tcp.port == 9999`: 40 packets
- Initial SYN packets: 20
- RST packets: 20
- Visible sequence: approximately 0.000000–0.089359 seconds in the relative capture timeline
- Interpretation: RST, ACK responses were consistent with local connection refusal. The traffic was deliberately generated for this lab, so it was benign test activity.

DNS, TCP handshake, UDP/QUIC, HTTP and TLS were verified across separate captures. Endpoints, Conversations and Follow TCP Stream evidence from Day 41 was reused rather than incorrectly presented as new Day 42 capture evidence.

## 💪 What went well

1. **I practised instead of only watching.** I generated DNS, HTTP, HTTPS/TLS and localhost connection traffic and inspected real packets.
2. **I learned to reduce noise.** I used filters for protocol, IP, port, TCP flags, TLS, retransmissions and duplicate ACKs.
3. **I connected packet-level evidence to conversations.** I compared packet counts with bytes and saw that the conversation with the most packets need not be the one with the most bytes.
4. **I made evidence-based conclusions.** In the Day 42 test, I documented repeated SYN/RST traffic as a controlled localhost experiment instead of calling it an attack.
5. **I corrected mistakes while working.** I fixed invalid display-filter syntax and adjusted interpretations after checking packet details.

## 🔧 What I need to improve

These are learning gaps to work on—not failures. The theory score of **7.75/10** is my current baseline, and I will compare future results against it.

### 1. Use precise networking language

During active recall, I initially needed help with endpoint vs. conversation and the exact meaning of RST.

- **Endpoint:** a network address/host entry with associated traffic statistics.
- **Conversation:** traffic exchanged between two endpoints, summarized with packets, bytes, duration and related details.
- **RST:** resets or rejects a TCP connection abruptly; it does not simply mean “the request is incomplete.”
- **FIN vs. RST:** FIN is used in orderly TCP shutdown; RST resets a connection.

**Practice:** Explain these four terms from memory before each study session until I can answer without a hint.

### 2. Explain the evidence, not just name fields

I can often find IPs, ports and flags, but the next step is to explain what each observation supports.

Use this sentence pattern:
- **Observation:** what the packet or statistic literally shows.
- **Interpretation:** what that evidence suggests.
- **Limit:** what cannot be concluded yet.
- **Next check:** what evidence would help confirm or reject the hypothesis.

Do not turn “port 443” into proof of HTTPS, “many connections” into proof of an attack, or “zero retransmissions” into proof that no packet loss occurred.

### 3. Read each packet on its own terms

One DNS capture contained HTTPS, AAAA and A queries. I should describe the selected packet's exact query type, then separately describe other rows, instead of combining adjacent packets into one answer.

**Practice:** For every chosen packet, read the packet number, source, destination, protocol, ports, flags or query type, and transaction/stream ID before writing a conclusion.

### 4. Improve report completeness

The Day 42 report was created, but the capture filename and wall-clock start time were not confirmed.

**Next time:** save the artifact with a clear name where appropriate, record the exact target/interface, filter or command, packet/row counts, timestamp or relative time range, and link the evidence file to the report. Keep sensitive PCAPs local unless they have been reviewed and sanitized.

### 5. Strengthen active recall

The Round 2 gaps were endpoint vs. conversation and RST interpretation. I improved after feedback, but I should retrieve these definitions independently before moving on.

**Practice:** end each session with a five-question closed-notes quiz. Revisit any answer scored below 4/5 the next session.

## 🎯 Week 7 improvement plan — Nmap + Network Enumeration

### Keep the same “learn briefly, do more” system

For a 2-hour study block:
- **20–25 min:** learn only the concept needed for today's task.
- **65–75 min:** run the lab, inspect the actual output, and troubleshoot.
- **10–15 min:** explain the result from memory.
- **10–15 min:** write the evidence and one thing still uncertain.

This keeps most of the session focused on application.

### Measurable targets for next week

- [ ] Perform at least **3 small Nmap exercises** against my own machine, own VM or an explicitly authorized lab.
- [ ] For each scan, record target, command, scan scope, result and timestamp.
- [ ] Explain the difference between open, closed and filtered without notes.
- [ ] Compare at least one scan result with locally observed listening services where possible.
- [ ] For each discovered port, separate the observed state from assumptions about the service or risk.
- [ ] Produce one short enumeration report containing evidence, interpretation, unknowns and next steps.
- [ ] Complete a short active-recall quiz; aim for **4/5 or better** on the main concepts.
- [ ] Review the Week 6 gaps (RST vs. FIN, endpoint vs. conversation, exact packet direction/type) before starting a new topic.

### Nmap investigation habit

1. Define the scope and confirm authorization before scanning.
2. Start with the smallest useful scan against a known lab target.
3. Record exact command and raw output; do not rely only on memory.
4. Explain what the output shows and what it does **not** show.
5. Correlate results with another source of evidence when possible.
6. Document one conclusion and one remaining question.

Do not scan public or third-party systems unless there is explicit authorization. Do not treat an open port as a vulnerability by itself.

## 📈 My personal scorecard

| Skill | Week 6 evidence | Next-week focus |
|---|---|---|
| Packet/protocol reading | Inspected DNS, TCP, UDP, HTTP and TLS | State direction and protocol details precisely |
| TCP analysis | Handshake, data, FIN, SYN and RST observed | Explain FIN vs. RST and connection state without hints |
| DNS analysis | Query/response and transaction ID correlated | Identify exact query type per packet |
| Wireshark filtering | Filtered by IP, port, flags, DNS and TLS | Keep distinguishing matched packets from connections |
| Follow TCP Stream | Used on captured TCP conversations | Explain when reassembly helps and when encryption still hides content |
| Endpoints/Conversations | Reviewed statistics and top traffic | Define endpoint vs. conversation cleanly |
| Evidence-based investigation | Wrote report on controlled SYN/RST sequence | Add complete metadata and an explicit evidence → interpretation → limit chain |
| Active recall | Day 42 theory test: **7.75/10** | Aim for 4/5 per main Week 7 topic; compare to this baseline |

## 🧠 The “me vs. me” rule

I do not need to be perfect or compare myself to another learner. I need to:
- keep proof of what I did;
- be honest about what I cannot explain yet;
- correct one or two recurring gaps each week;
- turn every lab into evidence and a written lesson;
- measure improvement by independent performance, not hours watched.

**Week 6 is complete. Week 7 starts with a baseline, a plan, and specific improvements—not a blank slate.**
