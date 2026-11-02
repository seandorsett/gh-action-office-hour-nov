# Rehearsal evidence

Executed November 2, 2026 in the private demo repository using GitHub-hosted
runners. These links preserve observed results, not promises of future availability.

| Demo | Observed outcome | Run |
|---|---|---|
| Preparation | Success: official generators compiled agent YAML and generated/verified actions.lock; artifact reviewed and committed | [41516641160](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516641160) |
| 01 - Lockfiles | Success: provenance verification passed; temporary new dependency was rejected by the offline coverage verifier | [41518464709](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518464709) |
| 02 - Agent preflight | Explicit failure: COPILOT_GITHUB_TOKEN absent; no inference submitted | [41518471047](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518471047) |
| 03 - Safe event context | Success for workflow_dispatch; this does not establish PR or policy behavior | [41516648590](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516648590) |
| 03 - Real pull_request | Success: event ref was refs/pull/1/merge | [41519546419](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41519546419) |
| 03 - Real pull_request_target | Success: event ref was refs/heads/main and SHA matched the base commit | [41519546426](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41519546426) |
| 04 - Network readiness | Success: tests passed, live Meta API retrieved, summary published | [41516654977](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516654977) |

Agent inference remains pending owner authentication. The owner has chosen to
configure the secret directly in GitHub Settings. Never copy a CLI login token
into the repository as a substitute.

The harmless [rehearsal PR #1](https://github.com/seandorsett/gh-action-office-hour-nov/pull/1)
is intentionally open for the event-context walkthrough. It changes only a
plain-text fixture. Both event handlers succeeded without checking out PR
content. This is actual event evidence, not evidence of default-policy blocking.

## Live launch and fallbacks

All presenter workflows launch through the Actions tab's **Run workflow**
button. Workflow sources are on the default branch. The preparation artifact
is a regeneration path, not a step required for every demo run.

If a live run fails, show the corresponding saved run and explain its timestamp.
For AI inference, show source/compilation only until a genuine successful
report run exists; do not present invented output as an AI result.

The local Python report suite also passed all four tests. No production
policy, cloud-provider selection or corporate firewall settings were changed.
