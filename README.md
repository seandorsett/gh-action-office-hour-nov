# DXC GitHub Actions Office Hour

**November 10, 2026 | 50 minutes presentation and demo + 10 minutes Q&A**

Research snapshot: October 4-November 2, 2026. Announcements after November 2
are not included. See [the source-linked catalogue](UPDATE-CATALOG.md).

## Selected updates and agenda

| Minutes | Topic |
|---|---|
| 0-4 | Welcome, outcomes and release window |
| 4-16 | Workflow dependency lockfiles GA - explanation and demo |
| 16-31 | GitHub Agentic Workflows GA - explanation and demo |
| 31-39 | pull_request_target: safer execution and changed enforcement dates |
| 39-46 | Multi-cloud compute and blob-storage network readiness |
| 46-50 | Takeaways, adoption checklist and buffer |
| 50-60 | Q&A |

This is a private, synthetic demo repository. It contains no production
applications or customer data. No workflow deploys cloud infrastructure.

## Browser-only demo launch

Open [Actions](https://github.com/seandorsett/gh-action-office-hour-nov/actions),
select a numbered workflow, choose **Run workflow**, retain the default branch,
and open the resulting run's **Summary** and job logs.

| Workflow | Purpose | Prerequisite |
|---|---|---|
| 00 - Prepare generated demo files | Compile agent source and generate actions.lock; publish reviewed files as an artifact | Maintainer reviews and commits generated output before demos |
| 01 - Workflow dependency lockfiles | Verify locked action provenance and detect controlled local dependency drift | Committed actions.lock |
| 02 - Agentic workflow preflight | Fail clearly when Copilot credentials or compiled YAML are missing | Repository secret configured by owner |
| Repo status office hour | Run agent and create at most one report issue | Compiled YAML, valid Copilot authentication, entitlement and AI budget |
| 03 - Safe event context | Inspect event metadata without checkout or secrets | Manual run works immediately; real PR comparison requires a PR |
| 04 - Multi-cloud and blob readiness | Retrieve public Meta API data and publish a network-readiness summary | No custom secrets |

No presenter terminal is needed during the meeting. GitHub-hosted runners
execute demo commands. Actions usage and AI inference may incur charges.

## Important distinctions

- `actions.lock` is the action dependency lockfile. Agentic `*.lock.yml`
  files are compiled workflow YAML, not the same mechanism.
- Demo 01's temporary drift check is **CLI validation**, not a fabricated
  server-side rejection. Initial checkout executes using the committed lock.
- Default `pull_request_target` blocking concerns **public** repositories,
  not this private repository. November 9 and 16 brownouts run 16:00-18:00 UTC;
  permanent enforcement begins December 2. November 10 is after the first
  brownout, not itself an enforcement window.
- A hosted Linux run cannot force a cloud provider or prove failover.
- A successful job summary does not prove DXC's corporate firewall readiness.

## Agent authentication

The Copilot engine requires a Copilot license. An owner must configure repository
secret `COPILOT_GITHUB_TOKEN` through **Settings > Secrets and variables > Actions**,
following the official
[authentication instructions](https://github.github.com/gh-aw/setup/quick-start/).
Do not paste tokens into source, chat, logs or issues.

The implementation uses the secret-based path. Organization-centralized Copilot
billing is an alternative requiring different permissions and an organization
subscription; it is not implicitly configured in this personal repository.
Check AI and Actions budgets before running. Workflows are manual, not scheduled.
The agent can read this demo repository and request one issue through safe
outputs; it cannot edit code or merge PRs.

## Presenter resources

- [PowerPoint deck](PRESENTATION.md)
- [Runbook and talking notes](PRESENTER-RUNBOOK.md)
- [Announcement catalogue and primary sources](UPDATE-CATALOG.md)
- [Rehearsal results and fallback runs](REHEARSAL.md)
