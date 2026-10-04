# Day 34 — Common Attacks + MITRE ATT&CK
**Planned date:** 2026-09-26

## Phishing
Attacker → fake email/message → victim → malicious link/attachment → credential theft or malware.

SOC indicators:
- Suspicious sender
- Suspicious domain
- Malicious attachment
- Unusual link
- Credential-harvesting page

## Brute force
Many passwords → one account.

## Password spraying
One/few common passwords → many accounts.

## Malware
High-level categories:
- Virus
- Worm
- Trojan
- Ransomware
- Spyware

## Credential theft
Stealing authentication information such as passwords, tokens or session information.

## MITRE ATT&CK
A knowledge base of adversary behavior based on real-world observations.

```text
TACTIC → Why / objective
TECHNIQUE → How
PROCEDURE → Specific implementation
```

## SOC mapping
Phishing → Credential Phishing → Credential Access

## Day 34 result
**19/20** on the test. Main gap identified: definition of MITRE ATT&CK itself; tactic/technique/procedure distinction was understood.