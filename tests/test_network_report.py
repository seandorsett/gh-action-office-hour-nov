import unittest

from scripts.network_report import build_report


class NetworkReportTests(unittest.TestCase):
    def test_valid_report_explains_limits_and_host_ranges(self):
        report = build_report({"actions": ["192.0.2.0/24", "2001:db8::/32"]})
        self.assertIn("**2**", report)
        self.assertIn("productionresultssa30-49", report)
        self.assertIn("productionresultssa100-199", report)
        self.assertIn("does not prove AWS placement", report)
        self.assertIn("DOES NOT prove", report)
        self.assertIn("observed: 0", report)

    def test_missing_empty_or_wrong_type_ranges_are_errors(self):
        for value in ({}, {"actions": []}, {"actions": "192.0.2.0/24"},
                      {"actions": [1]}, {"actions": ["not-a-network"]}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_report(value)

    def test_sample_is_not_full_allowlist(self):
        report = build_report({"actions": [f"192.0.{i}.0/24" for i in range(7)]})
        self.assertIn("**7**", report)
        self.assertIn("192.0.4.0/24", report)
        self.assertNotIn("192.0.5.0/24", report)
        self.assertIn("not a complete allowlist", report)

    def test_optional_domains_shape_is_validated(self):
        for domains in ("bad", {"actions": "bad"}):
            with self.subTest(domains=domains), self.assertRaises(ValueError):
                build_report({"actions": ["192.0.2.0/24"], "domains": domains})


if __name__ == "__main__":
    unittest.main()
