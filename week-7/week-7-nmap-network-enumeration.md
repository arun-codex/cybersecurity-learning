# 🛡️ WEEK 7 — NMAP + NETWORK ENUMERATION

## SOC / Blue Team Learning Plan

**Roadmap:** Month 2 — Week 7
**Study days:** Days 43–49
**Study time:** 11:00 PM–1:00 AM
**Friday:** 11:00 PM–12:00 AM
**Primary OS:** Fedora Linux
**Previous week:** Wireshark and packet analysis — completed
**Theory baseline:** Day 42 score = 7.75/10
**Next goal:** Learn to discover hosts, identify port states, recognize services, interpret scan results, and write a defensible network enumeration report.

---

# 🎯 1. THE MISSION FOR THIS WEEK

By Sunday, I should be able to answer:

> Which hosts are reachable in my authorized lab, which ports are open or closed, what services may be listening, and what does the evidence actually tell me?

I will learn:

- [ ] What Nmap is and how network enumeration works.
- [ ] Host discovery versus port scanning.
- [ ] TCP ports and common services.
- [ ] Open, closed, and filtered port states.
- [ ] Basic Nmap scan options.
- [ ] Service and version detection.
- [ ] How to save scan output.
- [ ] How to verify Nmap results using Linux commands and, where useful, Wireshark.
- [ ] How to distinguish observations from assumptions.
- [ ] How to document a safe, authorized network scan.

**This is a Blue Team learning week.** I am learning how to understand network exposure and produce useful evidence, not how to scan random targets.

The official Nmap documentation explains that scan results reflect the responses Nmap receives; port states are not absolute properties of a port and can differ depending on the network path and filtering. This distinction is central to the week.

---

# 📚 2. RESOURCE LIBRARY — USE THESE, NOT RANDOM SEARCHES

Keep this section as your resource index. Each day tells you exactly which resource to use and what to focus on.

## Resource A — Nmap beginner video

**The Techzeen — Cyber Security Tutorial #18: Nmap — Zero to Hero Network Scanning**

[https://www.youtube.com/watch?v=QcgPmNqQM2c](https://www.youtube.com/watch?v=QcgPmNqQM2c)

Use selected sections only:

- Host discovery and basic scanning.
- Common ports and services.
- Service/version detection.
- Saving scan output.

Skip advanced exploitation, NSE vulnerability scripts, evasion techniques, and full-port scanning for now.

## Resource B — Official Nmap guide

**Nmap Network Scanning — Official Guide**

[https://nmap.org/book/toc.html](https://nmap.org/book/toc.html)

Use these chapters throughout the week:

- [Host Discovery](https://nmap.org/book/man-host-discovery.html)
- [Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Service and Version Detection](https://nmap.org/book/man-version-detection.html)
- [Saving and Reading Scan Output](https://nmap.org/book/man-output.html)

## Resource C — Official explanation of port states

**Nmap: Port Scanning Basics**

[https://nmap.org/book/man-port-scanning-basics.html](https://nmap.org/book/man-port-scanning-basics.html)

Use this when learning:

- `open`
- `closed`
- `filtered`
- Why scan results can be incomplete.
- Why an open port does not automatically mean a vulnerability exists.

## Resource D — Fedora installation

**Official Nmap installation guide**

[https://nmap.org/book/inst-linux.html](https://nmap.org/book/inst-linux.html)

First check whether Nmap is installed. On Fedora, use DNF rather than copying Kali or Ubuntu installation commands.

## Resource E — MITRE ATT&CK

[https://attack.mitre.org/](https://attack.mitre.org/)

This week, use it only if you want to connect network discovery to a broader security investigation. Do not spend hours studying ATT&CK techniques.

---

# 🧠 3. MY LEARNING RULES

My preferred approach is approximately **20% consumption and 80% application**.

Each two-hour session should generally follow this pattern:

```text
10–20 minutes: targeted video or reading
        ↓
10 minutes: explain the concept from memory
        ↓
60–75 minutes: hands-on lab
        ↓
15–20 minutes: analyze evidence and document
        ↓
5 minutes: score confidence and record mistakes
```

Friday is shorter, so its activities are reduced.

### Rules I must follow

1. Attempt the task before looking at a walkthrough.
2. Use only my own machine, localhost, my own VM, or a target I have explicit permission to scan.
3. Record the exact command and actual output.
4. Never invent results to complete a report.
5. Separate what I observed from what I infer.
6. If a command fails, investigate the error instead of blindly copying another command.
7. Keep the scan scope small.
8. No advanced scan options until I understand the basic results.

---

# 📅 DAY 43 — MONDAY

# NMAP INSTALLATION, PURPOSE + FIRST SCAN

**Time:** 11:00 PM–1:00 AM
**Focus:** Understand the tool before learning lots of flags.

## 🎥 11:00–11:15 — Watch a focused section

Open Resource A:

[https://www.youtube.com/watch?v=QcgPmNqQM2c](https://www.youtube.com/watch?v=QcgPmNqQM2c)

Watch the introduction and basic port-scanning sections only.

Answer:

- What problem does Nmap solve?
- What is network enumeration?
- What is a host?
- What is a port?
- What is a service?

Do not watch the entire video tonight.

## 11:15–11:25 — Check installation

In Fedora Terminal:

```bash
nmap --version
```

If Nmap is not installed:

```bash
sudo dnf install nmap
```

Then verify:

```bash
nmap --version
```

If installation fails, record the exact error. Do not try random installation scripts.

## 11:25–11:35 — Break

## 11:35–11:50 — Understand the output

Read the official port-scanning overview:

[https://nmap.org/book/port-scanning.html](https://nmap.org/book/port-scanning.html)

Learn the difference between:

```text
Host discovery
    ↓
Is a host apparently reachable?

Port scanning
    ↓
What is the observed state of a port?

Service detection
    ↓
What service may be listening?
```

These are related but different questions.

## 11:50–12:10 — First local scan

Start with your own computer:

```bash
nmap 127.0.0.1
```

This scans the default set of common TCP ports on localhost.

Then run a small, explicitly scoped scan:

```bash
nmap -p 22,80,443,8000,9999 127.0.0.1
```

Record:

```text
Target:
Command:
Host status:
Ports reported:
Scan duration:
```

**Important:** Results depend on which services are listening and your local environment. Your output may differ from examples or tutorials.

## 12:10–12:30 — Verify with Linux

Run:

```bash
ss -lnt
```

Then:

```bash
ss -lnu
```

Understand:

- `ss` can show local listening sockets.
- Nmap probes ports and interprets responses.
- These commands do not necessarily show identical results because their scope and perspective differ.

If you see an unexpected port, do not assume it is malicious. Identify the process and purpose first.

## 12:30–12:45 — Evidence exercise

Choose one port from your scan.

Complete:

```text
Port:
Protocol:
Nmap state:
Possible service:
What the result directly tells me:
What it does NOT prove:
What I could check next:
```

## 12:45–12:55 — Active recall

Close your notes and answer:

1. What is Nmap?
2. What is enumeration?
3. What is a port?
4. How is a host different from a service?
5. What is the difference between host discovery and port scanning?
6. What does `nmap 127.0.0.1` do?

## 12:55–1:00 — Record progress

Create:

```text
week-7/day-43-first-scan.md
```

**Day 43 success condition**

- [ ] Nmap is installed or the installation error is documented.
- [ ] I ran a scan against localhost.
- [ ] I can explain the command I used.
- [ ] I recorded real output.
- [ ] I can explain one result without claiming more than the evidence supports.

---

# 📅 DAY 44 — TUESDAY

# HOST DISCOVERY + TARGET SCOPE

**Time:** 11:00 PM–1:00 AM
**Focus:** Discover hosts separately from scanning their ports.

## 🎥 11:00–11:15 — Read the official guide

Open:

[https://nmap.org/book/man-host-discovery.html](https://nmap.org/book/man-host-discovery.html)

Focus on:

- Host discovery.
- The `-sn` option.
- Why a host might not respond to a probe.
- Why an apparently down host may still be online.

Do not memorize all the discovery options.

## 11:15–11:25 — Recall

Without notes, explain:

- What is host discovery?
- What does a response tell me?
- Why might a host not respond?

## 11:25–11:35 — Break

## 11:35–11:50 — Inspect your own machine's network

Run:

```bash
ip -br address
```

Then:

```bash
ip route
```

Record:

```text
My active interface:
My local IPv4 address:
My subnet/prefix:
My default route:
```

Do not publish your private network details unnecessarily in public screenshots.

## 11:50–12:10 — Discover localhost

Run:

```bash
nmap -sn 127.0.0.1
```

This asks Nmap to perform host discovery without a normal port scan.

Compare with Day 43:

```text
Day 43: port-scanning results
Day 44: host-discovery results
```

Explain the difference.

## 12:10–12:30 — Optional isolated VM discovery

Only if you already have a lab VM running and know its IP:

```bash
nmap -sn <YOUR_AUTHORIZED_VM_IP>
```

Replace the placeholder with the IP of your own VM.

If you do not have a running VM, **skip this step**. Do not scan an arbitrary subnet or public IP range just to produce results.

## 12:30–12:45 — Investigate an unexpected result

If Nmap says a host appears down, ask:

1. Is the target IP correct?
2. Is the VM running?
3. Are both systems connected to a compatible virtual network?
4. Could a firewall or host-discovery probe affect the result?
5. What evidence could verify connectivity?

Do not jump straight to `-Pn`. First explain why the initial result might be incomplete.

## 12:45–12:55 — Active recall

1. What is the purpose of `-sn`?
2. Does host discovery enumerate all open ports?
3. Why might a live host fail to respond?
4. Why must I confirm the target address?
5. What is the difference between an observed host and an assumed host?

## 12:55–1:00 — Documentation

Create:

```text
week-7/day-44-host-discovery.md
```

Record your target, command, result, limitations, and conclusion.

**Day 44 success condition**

- [ ] I can explain host discovery.
- [ ] I used `-sn` against an authorized target.
- [ ] I understand why no response is not conclusive proof that a host is offline.
- [ ] I recorded my actual result.

---

# 📅 DAY 45 — WEDNESDAY

# PORT STATES + TCP CONNECTION REASONING

**Time:** 11:00 PM–1:00 AM
**Focus:** Learn the most important Nmap interpretation skill.

## 🎥 11:00–11:15 — Read

Open:

[https://nmap.org/book/man-port-scanning-basics.html](https://nmap.org/book/man-port-scanning-basics.html)

Focus on the three primary states:

- `open`
- `closed`
- `filtered`

You may encounter additional states later. Do not try to memorize all of them today.

## 11:15–11:25 — Recall the TCP flags

Use your Week 6 Wireshark knowledge.

```text
Client SYN
    ↓
Listening service SYN/ACK
    ↓
Client ACK
```

A TCP RST can indicate rejection or reset, depending on the context. It is not the same as an orderly FIN-based shutdown.

## 11:25–11:35 — Break

## 11:35–11:55 — Build a controlled local test

Start a temporary HTTP server in Terminal 1:

```bash
mkdir -p ~/cyber-lab/week7
cd ~/cyber-lab/week7
python3 -m http.server 8000 --bind 127.0.0.1
```

Leave this terminal running.

This server listens on localhost port 8000. It is intended for a local learning exercise, not a production service.

Open Terminal 2 and run:

```bash
nmap -p 8000 127.0.0.1
```

Record the state reported for TCP/8000.

## 11:55–12:10 — Compare a port with no listener

Run:

```bash
nmap -p 9999 127.0.0.1
```

Record the state reported for TCP/9999.

Do not assume that every machine will produce exactly the same result in every environment.

## 12:10–12:25 — Stop the local server

Return to Terminal 1 and press:

```text
Ctrl+C
```

Then run:

```bash
nmap -p 8000 127.0.0.1
```

Compare the before-and-after results.

The exercise should help you connect the observed state to whether an application was listening.

## 12:25–12:40 — Learn the interpretation table

| State      | Basic interpretation                                                                                                  |
| ---------- | --------------------------------------------------------------------------------------------------------------------- |
| `open`     | A service appears to accept connections or traffic on that port.                                                      |
| `closed`   | The target responds, but no application appears to be listening on that port.                                         |
| `filtered` | Nmap cannot determine whether the port is open because filtering or another network obstacle prevents a clear result. |

A state describes Nmap's view of the target from the scan's perspective; it is not a universal statement about every network path.

## 12:40–12:50 — Evidence versus inference

Complete:

```text
Observation:
Nmap reports TCP/8000 as open while my test server is running.

Supported interpretation:
________________________________

Unsupported conclusion:
________________________________

Additional evidence:
________________________________
```

Example of an unsupported conclusion: "The computer has been hacked because port 8000 is open."

## 12:50–1:00 — Active recall

1. What does `open` mean?
2. What does `closed` mean?
3. What does `filtered` mean?
4. Why can the same port look different from different networks?
5. Does an open port prove a vulnerability?
6. How does your Day 42 RST observation relate to connection refusal?

## Documentation

Create:

```text
week-7/day-45-port-states.md
```

**Day 45 success condition**

- [ ] I tested an open local port.
- [ ] I compared it with a port without a listener.
- [ ] I can explain the three primary port states.
- [ ] I distinguish evidence from assumptions.

---

# 📅 DAY 46 — THURSDAY

# BASIC SCAN OPTIONS + SERVICE DETECTION

**Time:** 11:00 PM–1:00 AM
**Focus:** Choose a suitable scan instead of memorizing flags blindly.

## 🎥 11:00–11:15 — Watch selected sections

Open Resource A:

[https://www.youtube.com/watch?v=QcgPmNqQM2c](https://www.youtube.com/watch?v=QcgPmNqQM2c)

Focus on:

- Basic port scanning.
- Service/version detection.
- Saving output.

Skip advanced evasion, aggressive scanning, and vulnerability scripts.

## 11:15–11:25 — Read

Official service/version detection guide:

[https://nmap.org/book/man-version-detection.html](https://nmap.org/book/man-version-detection.html)

Understand that a service name inferred from a port number is not always proof of the exact application running there. Version detection uses additional probes to improve identification.

## 11:25–11:35 — Break

## 11:35–11:55 — Run a small port scan

Start the local HTTP server again in Terminal 1:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

In Terminal 2:

```bash
nmap -p 8000,9999 127.0.0.1
```

Record the states.

## 11:55–12:15 — Run service detection

Run:

```bash
nmap -sV -p 8000 127.0.0.1
```

Observe whether Nmap identifies the service.

Record:

```text
Target:
Port:
State:
Service name:
Version information, if shown:
What Nmap actually identified:
What remains uncertain:
```

Service detection may identify a service without producing a complete version string. That is a valid result.

## 12:15–12:30 — Compare basic and version scans

Compare:

```bash
nmap -p 8000 127.0.0.1
```

with:

```bash
nmap -sV -p 8000 127.0.0.1
```

Answer:

- What information did the second scan add?
- Did it take longer?
- What evidence supports the service identification?
- What would you check if the service result were unexpected?

## 12:30–12:45 — Review common scan options

| Command/option | Purpose                                                      |
| -------------- | ------------------------------------------------------------ |
| `nmap TARGET`  | Default scan of common TCP ports.                            |
| `-sn`          | Host discovery without a normal port scan.                   |
| `-p 80,443`    | Scan selected ports.                                         |
| `-p 1-1000`    | Scan a specified port range.                                 |
| `-sV`          | Probe open ports to identify services and possible versions. |
| `-oN file.txt` | Save readable normal output to a file.                       |
| `-oA prefix`   | Save results in several useful output formats.               |

You do not need to learn every Nmap option this week.

## 12:45–12:55 — Active recall

1. What does `-p` do?
2. What does `-sV` add?
3. Why might a service use a nonstandard port?
4. Why is a service name not always conclusive proof?
5. When would saving output help a SOC analyst?

## 12:55–1:00 — Documentation

Create:

```text
week-7/day-46-service-detection.md
```

Stop the temporary HTTP server with `Ctrl+C`.
**Day 46 success condition**

- [ ] I ran a small, scoped scan.
- [ ] I performed service detection on my local test server.
- [ ] I compared results.
- [ ] I can explain which extra information `-sV` provided.

---

# 📅 DAY 47 — FRIDAY

# LIGHT REVIEW: PORTS, SERVICES + TCP STATES

**Time:** 11:00 PM–12:00 AM

Keep Friday light. No new large topic.

## 11:00–11:10 — Recall from memory

Explain:

- Host discovery.
- Port scanning.
- Open versus closed.
- Filtered.
- Service detection.
- TCP SYN and RST.

Do not open your notes yet.

## 11:10–11:20 — Break

## 11:20–11:40 — Mini practical

Run:

```bash
nmap -p 22,80,443,8000,9999 127.0.0.1
```

Then:

```bash
ss -lnt
```

Compare the two outputs.

Do not expect them to be identical: Nmap reports scan observations, while `ss` reports local socket information.

Record one difference and explain a possible reason.

## 11:40–11:55 — Correct your mistakes

Open your Day 43–46 notes.

Write:

```text
Mistake or uncertainty:
Correct explanation:
Evidence:
What I will do differently:
```

Focus on precise terms, not rewriting all your notes.

## 11:55–12:00 — Set Saturday's objective

Prepare the target for your authorized lab scan. Confirm its IP and that you have permission to scan it.

**Day 47 success condition**

- [ ] I revised without watching a video.
- [ ] I compared Nmap and `ss`.
- [ ] I recorded one mistake or uncertainty.
- [ ] My Saturday target is clearly authorized.

---

# 📅 DAY 48 — SATURDAY

# CONTROLLED ENUMERATION LAB + WIRESHARK CORRELATION

**Time:** 11:00 PM–1:00 AM
**Focus:** Combine Nmap with your existing packet-analysis skills.

This is the main practical day of Week 7.

## 11:00–11:10 — Define the scope

Use one of these targets:

1. Your own localhost.
2. Your own running VM with a known IP.
3. Another lab target for which you have explicit permission.

If no VM is running, use localhost. Do not waste the session building a complicated lab.

Record:

```text
Lab target:
IP:
Ownership/authorization:
Purpose of scan:
Allowed scope:
```

## 11:10–11:25 — Start a controlled service

For a localhost lab, open Terminal 1:

```bash
mkdir -p ~/cyber-lab/week7
cd ~/cyber-lab/week7
python3 -m http.server 8000 --bind 127.0.0.1
```

Keep it running.

If using your own VM instead, use an existing service you understand and are authorized to test. Do not expose a temporary service to your wider network unnecessarily.

## 11:25–11:35 — Break

## 11:35–11:50 — Perform host discovery

For the localhost lab:

```bash
nmap -sn 127.0.0.1
```

Record the result and explain what this command did not test.

## 11:50–12:10 — Enumerate selected ports

Run:

```bash
nmap -p 22,80,443,8000,9999 127.0.0.1
```

Then:

```bash
nmap -sV -p 8000 127.0.0.1
```

If you are scanning a VM, substitute its verified IP and retain the same small port scope.

Do not use `-A`, `-p-`, vulnerability scripts, or broad subnet scans for this exercise.

## 12:10–12:25 — Save your evidence

For localhost:

```bash
nmap -sV -p 8000 127.0.0.1 -oA ~/cyber-lab/week7/day48-local-service
```

This saves the scan in multiple formats using a common filename prefix.

Inspect the readable result:

```bash
cat ~/cyber-lab/week7/day48-local-service.nmap
```

Record the exact command and the actual output.

## 12:25–12:40 — Wireshark correlation

Open Wireshark and capture on the **loopback interface (`lo`)** if using localhost.

Run a small scan again:

```bash
nmap -p 8000,9999 127.0.0.1
```

Useful display filters:

```text
tcp.port == 8000
```

```text
tcp.port == 9999
```

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

```text
tcp.flags.reset == 1
```

The filters show packets matching those conditions. They do not directly tell you the total number of application-level connections.

Correlate:

```text
Nmap scan
    ↓
Observed packets
    ↓
TCP flags and responses
    ↓
Port state
    ↓
Careful interpretation
```

If loopback capture does not show what you expect, record that limitation and check the selected interface and capture settings. Do not fabricate a packet result.

## 12:40–12:50 — Write the investigation conclusion

Answer:

1. Which target did I scan?
2. Which ports did I test?
3. Which port states did Nmap report?
4. What service did Nmap identify?
5. What did Wireshark show?
6. Did packet evidence support the scan interpretation?
7. What remains unknown?

Remember: these observations come from your own controlled lab, not from a real external incident.

## 12:50–1:00 — Stop and save

Stop the local server with `Ctrl+C`.

Save your Wireshark capture only if useful and ensure it contains no unnecessary sensitive traffic.

Create:

```text
week-7/day-48-enumeration-lab.md
```

**Day 48 success condition**

- [ ] I used an authorized target.
- [ ] I performed host discovery or explained why I skipped it.
- [ ] I scanned a small, defined set of ports.
- [ ] I saved Nmap output.
- [ ] I correlated results with Wireshark where practical.
- [ ] I wrote a conclusion with limitations.

---

# 📅 DAY 49 — SUNDAY

# WEEK 7 ASSESSMENT + PORTFOLIO REPORT

**Time:** 11:00 PM–1:00 AM

Sunday measures what I can do independently. It is not another tutorial day.

## 11:00–11:20 — Closed-notes theory test

No YouTube, no Google, no notes, and no AI answers during this first attempt.

Answer in your own words:

1. What is Nmap?
2. What is network enumeration?
3. Host discovery versus port scanning?
4. What is a TCP port?
5. What does `open` mean?
6. What does `closed` mean?
7. What does `filtered` mean?
8. What does `-sn` do?
9. What does `-p` do?
10. What does `-sV` do?
11. Why might a service run on an unusual port?
12. Why does an open port not prove a vulnerability?
13. Why can Nmap and `ss` show different information?
14. Why is a missing response not enough to prove a host is offline?
15. What does Wireshark add to an Nmap investigation?

Score each answer:

```text
1 = Incorrect or blank
2 = Partially correct
3 = Correct but vague
4 = Accurate and clear
```

Convert the total to a percentage:

```text
Score percentage = points earned / 60 × 100
```

Compare this result with your Week 6 baseline of **7.75/10**. It is a useful reference, not a reason to inflate or lower your score.

## 11:20–11:30 — Break

## 11:30–11:55 — Independent practical

Without copying a previous command, plan and execute a small scan against localhost:

```bash
nmap -p 22,80,443,8000,9999 127.0.0.1
```

Then inspect:

```bash
ss -lnt
```

If you have your local HTTP server available, perform service detection:

```bash
nmap -sV -p 8000 127.0.0.1
```

If a command fails, record the failure and troubleshoot it. The goal is independent problem-solving, not a perfect-looking terminal.

Write down:

```text
What I intended to test:
Command:
Actual result:
What I observed:
What I infer:
What remains uncertain:
Next check:
```

## 11:55–12:20 — Write the final lab report

Create:

```text
week-7/nmap-network-enumeration-report.md
```

Use this template:

```markdown
# Nmap Network Enumeration Lab

## 1. Objective

What was I trying to learn?

## 2. Scope and Authorization

Target:
IP:
Why I was authorized to scan it:
Ports tested:

## 3. Environment

Operating system:
Nmap version:
Other tools used:

## 4. Commands

List each command exactly as executed.

## 5. Results

Port:
Protocol:
State:
Service:
Version, if identified:

## 6. Evidence

What did Nmap report?
What did `ss` report?
Was Wireshark used?
What packet details were relevant?

## 7. Interpretation

What do the results support?

## 8. Limitations

What could not be established?
Could filtering or the scan vantage point affect results?

## 9. Next Steps

What would I investigate next in a real authorized assessment?

## 10. Conclusion

Summarize the findings without claiming more than the evidence supports.
```

Use actual outputs. If a result was not observed, say so.

## 12:20–12:40 — Improve your report

Check:

- [ ] Target and authorization are explicit.
- [ ] Commands are exact.
- [ ] Results are not invented.
- [ ] Observations and interpretations are separate.
- [ ] Limitations are included.
- [ ] No unsupported claim of compromise or vulnerability appears.
- [ ] The report is readable by another learner or junior analyst.

## 12:40–12:50 — Week 6 mistake review

Return to your Week 6 review.

Explain without notes:

- Endpoint versus conversation.
- FIN versus RST.
- What a selected packet proves versus what other packets suggest.
- Why packet count is not connection count.
- Why a repeated connection attempt is not automatically malicious.

These are short maintenance reviews, not a repeat of the full Wireshark week.

## 12:50–1:00 — Score and commit

Score yourself:

| Skill                         | Score /5 |
| ----------------------------- | -------: |
| Nmap purpose and basic syntax |       /5 |
| Host discovery                |       /5 |
| Port states                   |       /5 |
| TCP connection reasoning      |       /5 |
| Service detection             |       /5 |
| Interpreting scan results     |       /5 |
| Using `ss` for verification   |       /5 |
| Wireshark correlation         |       /5 |
| Evidence vs inference         |       /5 |
| Independent recall            |       /5 |
| Report quality                |       /5 |

Commit the actual work to your cybersecurity learning repository.

Suggested commit:

```text
Week 7: Nmap enumeration lab and findings
```

**Day 49 success condition**

- [ ] I completed the closed-notes test.
- [ ] I ran a practical scan independently.
- [ ] I compared the result with local socket information.
- [ ] I wrote a lab report.
- [ ] I identified at least one remaining uncertainty or improvement.

---

# 📂 4. WEEK 7 GITHUB STRUCTURE

Use your existing repository, `arun-codex/cybersecurity-learning`, rather than creating a duplicate repository.

Suggested structure:

```text
cybersecurity-learning/
└── week-7/
    ├── day-43-first-scan.md
    ├── day-44-host-discovery.md
    ├── day-45-port-states.md
    ├── day-46-service-detection.md
    ├── day-48-enumeration-lab.md
    └── nmap-network-enumeration-report.md
```

You do not need six long documents. Short notes with real commands, output, interpretations, and limitations are enough.

Never publish sensitive addresses, credentials, or unrelated traffic captures. Use sanitized evidence where necessary.

---

# 🧪 5. QUICK NMAP REFERENCE

Keep this small cheat sheet for the lab.

| Command                          | Purpose                                      |
| -------------------------------- | -------------------------------------------- |
| `nmap --version`                 | Check the installed version                  |
| `nmap 127.0.0.1`                 | Scan common TCP ports on localhost           |
| `nmap -sn 127.0.0.1`             | Host discovery without a normal port scan    |
| `nmap -p 80,443 127.0.0.1`       | Scan selected ports                          |
| `nmap -sV -p 8000 127.0.0.1`     | Probe a port for service/version information |
| `nmap -oN results.txt 127.0.0.1` | Save normal output                           |
| `nmap -oA results 127.0.0.1`     | Save results in several formats              |
| `ss -lnt`                        | Inspect local listening TCP sockets          |
| `ss -lnu`                        | Inspect local listening UDP sockets          |

These commands are for the authorized lab scope described in this plan. Do not add public targets or broader ranges without explicit authorization.

---

# 🧠 6. MY EVIDENCE-BASED REASONING CHECKLIST

Every time I inspect a scan result, I will ask:

### Observation

What did the tool literally report?

### Interpretation

What is the most reasonable explanation?

### Uncertainty

What can this result not establish?

### Verification

Which second source or practical test could help?

### Next action

What is the smallest useful next check?

Example:

```text
Observation:
TCP/8000 is reported open on localhost.

Interpretation:
A local service appears to be accepting connections.

Uncertainty:
This does not establish that the service is vulnerable or malicious.

Verification:
Check the listening socket and identify the process.

Next action:
Determine whether the service is expected and needed.
```

This is the mindset I want to carry into SOC investigations.

---

# 🏁 7. WEEK 7 DEFINITION OF DONE

Week 7 is complete when I can:

- [ ] Explain Nmap and network enumeration in simple language.
- [ ] Explain host discovery versus port scanning.
- [ ] Interpret open, closed, and filtered states.
- [ ] Run a basic scan against an authorized target.
- [ ] Scan selected ports.
- [ ] Perform basic service/version detection.
- [ ] Verify local listening sockets using `ss`.
- [ ] Explain why Nmap and local socket output may differ.
- [ ] Save scan results.
- [ ] Produce one clear network enumeration report.
- [ ] Explain what the evidence proves and what remains uncertain.
- [ ] Answer my previous weak Wireshark questions without hints.

If I cannot do one of these independently, I record it as a revision item. I do not pretend I mastered it simply because I completed the calendar.

---

# 🚫 8. WHAT I WILL NOT DO THIS WEEK

I will not:

- Install Kali just to run Nmap.
- Scan random public IP addresses.
- Scan my workplace, university, or other people's networks without permission.
- Run aggressive scans against unknown targets.
- Run vulnerability scripts or attempt exploitation.
- Memorize dozens of flags without understanding them.
- Claim a system is vulnerable based only on an open port.
- Claim an attack based only on repeated connection attempts.
- Spend the entire week watching tutorials.
- Make up output to complete a report.

The objective is accurate, safe, defensible analysis.

---

# 🎯 9. WHAT COMES NEXT — WEEK 8

The roadmap moves to **OWASP basics + DBMS security**, including high-level web vulnerability categories, SQL injection concepts, and an intentionally vulnerable lab such as OWASP Juice Shop.

Week 7 prepares me to understand which network services are exposed. Week 8 will help me understand common web application risks and how to describe the relationship between:

```text
Potential vulnerability
        ↓
Evidence
        ↓
Impact
        ↓
Mitigation
```

I will not skip the evidence and impact steps.

---

# 🛡️ FINAL PRINCIPLE

**My goal is not to become the person who runs the most Nmap commands.**

My goal is to become the person who can explain:

- Why a scan was run.
- What the results show.
- What the results do not show.
- What evidence is needed next.
- How to communicate findings clearly.

**This is me versus me: use the Week 6 baseline, correct my gaps, and prove my improvement through independent work.**
