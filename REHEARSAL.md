# Rehearsal evidence

Executed November 2, 2026 in the private demo repository using GitHub-hosted
runners. These links preserve observed results, not promises of future availability.

| Demo | Observed outcome | Run |
|---|---|---|
| Preparation | Success: official generators compiled agent YAML and generated/verified actions.lock; artifact reviewed and committed | [41516641160](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41516641160) |
| 01 - Lockfiles | Success: provenance verification passed; temporary new dependency was rejected by the offline coverage verifier | [41518464709](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518464709) |
| 02 - Agent preflight | Explicit failure: COPILOT_GITHUB_TOKEN absent; no inference submitted | [41518471047](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/41518471047) |

Additional Agentic Workflow rehearsal on November 5, 2026:

| Demo | Observed outcome | Run |
|---|---|---|
| 02 - Agentic workflow preflight | Success: expected Copilot secret name and compiled workflow validated; secret value was not accessed | [42130203122](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/42130203122) |
| Repo status office hour | Success: all five jobs completed; Copilot inference ran and the bounded safe-output job created the report below | [42130308648](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/42130308648) |
| Generated report | Success: synthetic repository report created; review its time-of-run caveats before presenting | [Issue #2](https://github.com/seandorsett/gh-action-office-hour-nov/issues/2) |

The secret value was never read or exposed. A successful rehearsal does not
guarantee future Copilot entitlement, budget or service availability. Never copy
a CLI login token into the repository as a substitute.

The issue-triage example in the presentation is illustrative and was not
rehearsed as a runnable workflow. The live Agentic Workflow evidence above is
for the repository-status report.

## Live launch and fallbacks

All presenter workflows launch through the Actions tab's **Run workflow**
button. Workflow sources are on the default branch. The preparation artifact
is a regeneration path, not a step required for every demo run.

If a live run fails, show the corresponding saved run and explain its timestamp.
For AI inference, show source/compilation only if no genuine successful report
run is available; do not present invented output as an AI result.

No production policy, cloud-provider selection or corporate firewall settings
were changed.
