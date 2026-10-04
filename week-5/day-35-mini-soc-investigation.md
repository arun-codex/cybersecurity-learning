# 🛡️ Day 35 — Week 5 Integration + Mini SOC Investigation
**Planned date:** 2026-09-27
**Status:** ✅ Completed

## Topics covered

### CIA Triad
- **Confidentiality** → Who can see the data?
- **Integrity** → Was the data changed improperly?
- **Availability** → Can the system/data be used when needed?

### AAA
- **Authentication** → Who are you?
- **Authorization** → What are you allowed to do?
- **Accounting** → What did you do?

### Least Privilege
Give a user or process only the permissions required to perform its job.

**Example:** A web server needs access to website files but does not need full root access.

### Defense in Depth
Do not depend on one security control.

Example layers:
`Firewall → Authentication → Permissions → Endpoint Security → Logging → Backups`

### Threat Language
- **Threat** → Something capable of causing harm
- **Vulnerability** → A weakness
- **Exploit** → Method/code/action that takes advantage of a weakness
- **Risk** → Potential impact considering likelihood
- **IOC** → Evidence/artifact that may indicate compromise
- **TTP** → Tactics, Techniques and Procedures

### TTP mental model
- **Tactic** → WHY / objective
- **Technique** → HOW
- **Procedure** → Specific implementation

## Common attacks reviewed

### Phishing
Attacker → fake email/message → victim → malicious link/attachment → credential theft or malware

### Brute Force
Trying many passwords against a target account.

### Password Spraying
Trying one or a few common passwords against multiple accounts.

### Malware
Reviewed:
- Virus
- Worm
- Trojan
- Ransomware
- Spyware

## MITRE ATT&CK
- **Tactic = WHY / objective**
- **Technique = HOW**
- **Procedure = specific implementation**

## Mini SOC Investigation

### Observation
1. Multiple failed login attempts were observed.
2. A successful login followed the failed attempts.
3. This could indicate a brute-force-style authentication attack.
4. This is **not proof of compromise** by itself.
5. Further investigation is required.

### Next investigation ideas
- Check whether the login came from a known location.
- Check whether the device used for login is known/previously seen.
- Correlate with other activity, timestamps and logs.

## Analyst mindset
**Evidence → Observation → Hypothesis → More evidence → Conclusion**

The key lesson from Day 35: suspicious activity should trigger investigation, but conclusions should be based on evidence.

## My notes / answers

1. CIA = Confidentiality, Integrity, Availability.
2. Authentication proves who you are; authorization determines what you are allowed to do.
3. Accounting keeps track of activity such as logins, changes, access and logout.
4. Least privilege means giving only the access a user/process actually needs instead of root access.
5. Defense in depth means using multiple security controls so one failed control does not expose everything.
6. A threat is something capable of causing harm; a vulnerability is a weakness in a system.
7. An exploit is the method/action used to take advantage of a vulnerability.
8. Risk considers the potential impact together with likelihood.
9. An IOC is evidence/artifact that may indicate compromise.
10. TTP = Tactics, Techniques and Procedures.
11. Phishing flow: attacker → message → victim → malicious link/attachment.
12. Brute force: many passwords against one target; password spraying: one/few passwords across multiple users.
13. Phishing can lead to credential theft when a victim enters credentials into a fake site.
14. Malware includes categories such as virus, Trojan and worm.
15. MITRE ATT&CK can be used as a knowledge base for describing adversary behavior and organizing activity by why/how/specific implementation.
16. Tactic = attacker objective/motive.
17. Technique = how the attacker performs the activity.
18. Procedure = the specific implementation of the technique.
19. Security controls help prevent, detect and respond to attacks.
20. Ping can be used to test reachability and observe latency/loss.
21. Traceroute can show the path/hops between a source and destination, where responses are available.
22. A firewall is a set of rules used to allow or deny network traffic.

## Reflection
Day 35 connected the earlier networking/Linux work to a SOC-style way of thinking: observe activity, identify what is suspicious, avoid overclaiming, and decide what evidence should be checked next.
