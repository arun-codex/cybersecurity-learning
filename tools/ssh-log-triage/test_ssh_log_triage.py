import unittest

from ssh_log_triage import analyze_lines


class AnalyzeLinesTests(unittest.TestCase):
    def test_counts_failures_invalid_users_and_successes(self):
        lines = [
            "Oct 12 01:00:00 host sshd[100]: Failed password for root from 192.0.2.10 port 51222 ssh2",
            "Oct 12 01:00:01 host sshd[101]: Failed password for root from 192.0.2.10 port 51223 ssh2",
            "Oct 12 01:00:02 host sshd[102]: Failed password for invalid user guest from 192.0.2.10 port 51224 ssh2",
            "Oct 12 01:00:02 host sshd[102]: Invalid user guest from 192.0.2.10 port 51224",
            "Oct 12 01:01:00 host sshd[103]: Accepted publickey for arun from 2001:db8::1 port 44000 ssh2",
            "Oct 12 01:02:00 host CRON[555]: unrelated service event",
        ]

        report = analyze_lines(lines, threshold=3)

        self.assertEqual(report["summary"]["failed_auth_attempts"], 3)
        self.assertEqual(report["summary"]["accepted_logins"], 1)
        self.assertEqual(report["summary"]["invalid_user_events"], 1)
        self.assertEqual(report["failed_attempts_by_user"], {"guest": 1, "root": 2})
        self.assertEqual(report["accepted_logins_by_ip"], {"2001:db8::1": 1})
        self.assertEqual(len(report["alerts"]), 1)
        self.assertEqual(report["alerts"][0]["source_ip"], "192.0.2.10")
        self.assertEqual(report["alerts"][0]["severity"], "medium")

    def test_alert_severity_increases_at_twice_threshold(self):
        lines = [
            f"sshd[1]: Failed password for root from 198.51.100.7 port {40000 + i} ssh2"
            for i in range(6)
        ]
        report = analyze_lines(lines, threshold=3)
        self.assertEqual(report["alerts"][0]["severity"], "high")

    def test_ignores_malformed_addresses(self):
        lines = ["sshd[1]: Failed password for root from not-an-ip port 22 ssh2"]
        report = analyze_lines(lines, threshold=1)
        self.assertEqual(report["summary"]["failed_auth_attempts"], 0)
        self.assertEqual(report["alerts"], [])

    def test_threshold_must_be_positive(self):
        with self.assertRaises(ValueError):
            analyze_lines([], threshold=0)


if __name__ == "__main__":
    unittest.main()
