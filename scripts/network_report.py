import ipaddress
import json
import os
from pathlib import Path
import sys


def build_report(meta):
    ranges = meta.get("actions")
    if not isinstance(ranges, list) or not ranges:
        raise ValueError("Meta API must contain a nonempty actions IP range array")
    if not all(isinstance(value, str) for value in ranges):
        raise ValueError("Actions IP ranges must be strings")
    for value in ranges:
        ipaddress.ip_network(value)
    domains = meta.get("domains", {})
    if not isinstance(domains, dict):
        raise ValueError("Meta API domains must be an object when present")
    endpoints = domains.get("actions", [])
    if not isinstance(endpoints, list):
        raise ValueError("Meta API domains.actions must be an array when present")
    return "\n".join([
        "## Multi-cloud and blob-storage readiness", "",
        f"Current published Actions IP ranges: **{len(ranges)}**.",
        "Source: https://api.github.com/meta (retrieved by this workflow).", "",
        "Eligible Linux jobs can use expanded multi-cloud capacity; provider placement",
        "is automatic. This run does not prove AWS placement, failover or lower queue time.", "",
        "Enterprise Cloud requires opt-in. Do not automatically change organization policies.",
        "Review IP allowlists and conditional access; Azure-only ranges are insufficient.", "",
        "### First five published IP ranges (not a complete allowlist)", "",
        "```text", *ranges[:5], "```", "",
        "### Blob-storage announcement (October 22)", "",
        "New inclusive host ranges: productionresultssa30-49.blob.core.windows.net",
        "and productionresultssa100-199.blob.core.windows.net.",
        "These are host-number ranges, not literal DNS wildcard expressions.", "",
        f"Meta API domains.actions entries observed: {len(endpoints)}.",
        "Absence of a particular hostname in this response does not invalidate",
        "the announcement or establish firewall compliance.", "",
        "A successful summary proves this job can publish a summary. It DOES NOT prove",
        "DXC's network allows all endpoints or any particular new endpoint was used.", "",
        "### Operational checklist", "",
        "- Obtain the complete current Actions IP list from the API, not this sample.",
        "- Review firewall, proxy and identity access policies with their owners.",
        "- Synchronize published ranges through an approved network change process.",
        "- Preserve a successful run as the presentation fallback.", "",
    ])


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/network_report.py <meta.json>")
    report = build_report(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    print(report)
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
        summary.write(report)


if __name__ == "__main__":
    main()
