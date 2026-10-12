# SSH Authentication Log Triage

A small, offline Python utility for learning how a SOC analyst can triage common OpenSSH authentication events. It uses only the Python standard library, has unit tests, and makes no network connections.

## What it reports

- Failed password/public-key authentication attempts grouped by source IP and username.
- Accepted logins grouped by source IP and username.
- Invalid user events grouped by source IP.
- A configurable alert when one source IP reaches the chosen failed-attempt threshold.
- JSON output suitable for retaining with a lab investigation.

## Run it

Requires Python 3.10+.

\`\`\`bash
python3 ssh_log_triage.py sample-auth.log --threshold 3
python3 ssh_log_triage.py sample-auth.log --threshold 3 --output report.json
\`\`\`

On Fedora, the system authentication log is commonly /var/log/secure; on Debian/Ubuntu it is commonly /var/log/auth.log. Read permission may be required. Start with the included sanitized sample before analyzing a real log.

## Test it

From this directory:

\`\`\`bash
python3 -m unittest -v
\`\`\`

## Analyst cautions

An alert is a lead for investigation, not a verdict. Failed logins may come from authorized testing, misconfigured clients, forgotten credentials, or hostile activity. Confirm source context and correlate with other evidence before escalating. This parser uses common OpenSSH text patterns and will not understand every distribution/version or every authentication method. Keep reports protected: usernames, source IPs, and authentication events can be sensitive operational data.

Only analyze logs you are authorized to access. This tool does not block IPs, attempt logins, or perform scanning.
