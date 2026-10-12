#!/usr/bin/env python3
"""Offline triage for common OpenSSH authentication log events.

Uses only the Python standard library. It does not connect to hosts, modify logs,
block IPs, or make claims that an event is malicious.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

_FAILED_RE = re.compile(
    r"\bFailed\s+(?:password|publickey|keyboard-interactive/pam)\s+for\s+"
    r"(?:(?:invalid|illegal)\s+user\s+)?(?P<user>\S+)\s+from\s+"
    r"(?P<ip>\S+)\s+port\s+(?P<port>\d+)\b",
    re.IGNORECASE,
)
_ACCEPTED_RE = re.compile(
    r"\bAccepted\s+(?:password|publickey|keyboard-interactive/pam)\s+for\s+"
    r"(?P<user>\S+)\s+from\s+(?P<ip>\S+)\s+port\s+(?P<port>\d+)\b",
    re.IGNORECASE,
)
_INVALID_USER_RE = re.compile(
    r"(?<!for )\bInvalid user\s+(?P<user>\S+)\s+from\s+(?P<ip>\S+)\b",
    re.IGNORECASE,
)


def _normalise_ip(value: str) -> str | None:
    """Return a canonical IP address, or None for malformed/non-IP input."""
    try:
        return str(ipaddress.ip_address(value))
    except ValueError:
        return None


def _sorted_counts(counter: Counter[str]) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def analyze_lines(lines: Iterable[str], threshold: int = 5) -> dict[str, object]:
    """Summarize SSH authentication events from log lines.

    Args:
        lines: Iterable of syslog/auth.log lines.
        threshold: Minimum failed attempts from one IP that creates an alert.

    Returns:
        A JSON-serializable report. Raw log lines are deliberately not retained.
    """
    if threshold < 1:
        raise ValueError("threshold must be at least 1")

    failures_by_ip: Counter[str] = Counter()
    failures_by_user: Counter[str] = Counter()
    accepted_by_ip: Counter[str] = Counter()
    accepted_by_user: Counter[str] = Counter()
    invalid_users_by_ip: Counter[str] = Counter()
    total_invalid_users = 0

    for line in lines:
        failed_match = _FAILED_RE.search(line)
        if failed_match:
            source_ip = _normalise_ip(failed_match.group("ip"))
            if source_ip:
                failures_by_ip[source_ip] += 1
                failures_by_user[failed_match.group("user")] += 1

        accepted_match = _ACCEPTED_RE.search(line)
        if accepted_match:
            source_ip = _normalise_ip(accepted_match.group("ip"))
            if source_ip:
                accepted_by_ip[source_ip] += 1
                accepted_by_user[accepted_match.group("user")] += 1

        invalid_match = _INVALID_USER_RE.search(line)
        if invalid_match:
            source_ip = _normalise_ip(invalid_match.group("ip"))
            if source_ip:
                invalid_users_by_ip[source_ip] += 1
                total_invalid_users += 1

    alerts = [
        {
            "source_ip": source_ip,
            "failed_attempts": count,
            "severity": "high" if count >= threshold * 2 else "medium",
            "reason": (
                f"{count} failed SSH authentication attempts from this IP; "
                f"configured threshold is {threshold}."
            ),
        }
        for source_ip, count in sorted(failures_by_ip.items())
        if count >= threshold
    ]

    return {
        "summary": {
            "failed_auth_attempts": sum(failures_by_ip.values()),
            "accepted_logins": sum(accepted_by_ip.values()),
            "invalid_user_events": total_invalid_users,
            "unique_failure_source_ips": len(failures_by_ip),
            "alert_threshold_per_ip": threshold,
        },
        "failed_attempts_by_ip": _sorted_counts(failures_by_ip),
        "failed_attempts_by_user": _sorted_counts(failures_by_user),
        "accepted_logins_by_ip": _sorted_counts(accepted_by_ip),
        "accepted_logins_by_user": _sorted_counts(accepted_by_user),
        "invalid_users_by_ip": _sorted_counts(invalid_users_by_ip),
        "alerts": alerts,
        "limitations": [
            "This is simple pattern matching, not a complete SSH log parser.",
            "A high failure count is a triage signal, not proof of malicious activity.",
            "Log formats vary; verify findings against the original records.",
            "Reports may contain usernames and IP addresses; protect them as sensitive data.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Summarize common SSH authentication events from an auth log."
    )
    parser.add_argument(
        "logfile", type=Path, help="Path to auth.log/secure or a sanitized sample"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Failed attempts from one source IP needed for an alert (default: 5)",
    )
    parser.add_argument(
        "--output", type=Path, help="Write JSON report to this file instead of stdout"
    )
    args = parser.parse_args(argv)

    if args.threshold < 1:
        parser.error("--threshold must be at least 1")

    try:
        with args.logfile.open("r", encoding="utf-8", errors="replace") as handle:
            report = analyze_lines(handle, threshold=args.threshold)
    except OSError as exc:
        print(f"error: cannot read {args.logfile}: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        try:
            args.output.write_text(rendered, encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot write {args.output}: {exc}", file=sys.stderr)
            return 2
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
