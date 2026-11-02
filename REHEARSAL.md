# Rehearsal evidence

Executed November 2, 2026 in the private demo repository using GitHub-hosted
runners. These links preserve observed results, not promises of future availability.

| Demo | Observed outcome | Run |
|---|---|---|
| Preparation | Success: official generators compiled agent YAML and generated/verified actions.lock; artifact reviewed and committed | [41516641160](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516641160) |
| 01 - Lockfiles | Success: provenance verification passed; temporary new dependency was rejected by the offline coverage verifier | [41518464709](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518464709) |
| 02 - Agent preflight | Explicit failure: COPILOT_GITHUB_TOKEN absent; no inference submitted | [41518471047](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518471047) |
| 03 - Safe event context | Success for workflow_dispatch; this does not establish PR or policy behavior | [41516648590](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516648590) |
| 04 - Network readiness | Success: tests passed, live Meta API retrieved, summary published | [41516654977](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516654977) |

Agent inference remains pending owner authentication. The owner has chosen to
configure the secret directly in GitHub Settings. Never copy a CLI login token
into the repository as a substitute.

## Live launch and fallbacks

All presenter workflows launch through the Actions tab's **Run workflow**
button. Workflow sources are on the default branch. The preparation artifact
is a regeneration path, not a step required for every demo run.

If a live run fails, show the corresponding saved run and explain its timestamp.
For AI inference, show source/compilation only until a genuine successful
report run exists; do not present invented output as an AI result.

The local Python report suite also passed all four tests. No production
policy, cloud-provider selection or corporate firewall settings were changed.
