# DXC GitHub Actions Office Hour

**November 10, 2026 | 60 minutes**

This private repository supports the office hour with two selected updates:
GitHub Actions workflow dependency lockfiles and GitHub Agentic Workflows.
The demos use synthetic repository content; they do not deploy infrastructure
or access production applications.

## Agenda

| Minutes | Topic |
|---|---|
| 0-5 | Welcome and context |
| 5-10 | Workflow dependency lockfiles |
| 10-50 | Agentic Workflows deep dive and live demo |
| 50-60 | Q&A |

## Run the presentation demos

All demos run on GitHub-hosted runners from the repository's **Actions** tab:
select the workflow, choose **Run workflow**, keep the default branch, then
review the run summary and logs.

| Presentation segment | Workflow | What it demonstrates |
|---|---|---|
| Workflow dependency lockfiles | **01 - Workflow dependency lockfiles** | Verifies the committed action lockfile and shows the verifier rejecting controlled, temporary dependency drift without changing the branch |
| Agentic Workflows | **Issue triage office hour** | Enter one open synthetic issue number; a read-only agent reviews only that issue and requests at most one separate triage report issue through a safe-output job. The source issue is not changed. |
| Agentic Workflows (alternate) | **Repo status office hour** | Compiles and runs a read-only agent against repository activity, then requests one bounded report issue through a separate safe-output job |

Issue triage requires Copilot inference authentication and an open synthetic
issue to select. It has been compiled but not yet rehearsed with live inference;
use the repository-status report as the rehearsed fallback.

## Support workflows

- **00 - Prepare generated demo files** is a maintainer utility for compiling
  both Agentic Workflows and regenerating/verifying the action lockfile. Review
  its artifact and commit generated files before a presentation; it does not
  push changes.
- **02 - Agentic workflow preflight** checks that the compiled workflow and
  repository secret are present. It does not validate the token or submit an
  AI request.

## Agent authentication

The Copilot engine requires an eligible Copilot license. The configured
secret-based path uses a fine-grained personal access token with only the
**Copilot Requests: Read** account permission, stored as the repository secret
`COPILOT_GITHUB_TOKEN`. Do not add repository-content permissions to that
token or paste credentials into source, chat, logs, or issues. See the official
[quickstart](https://github.github.com/gh-aw/setup/quick-start/) and
[authentication reference](https://github.github.com/gh-aw/reference/auth/#github-copilot-default).

Check Copilot entitlement and AI/Actions budgets before running. The agent has
read-only repository access; a separate safe-output job can create at most one
issue. The workflow is manually triggered, not scheduled.

## Presenter resources

- [PowerPoint deck](PRESENTATION.md)
- [Runbook and talking notes](PRESENTER-RUNBOOK.md)
- [Announcement catalogue and primary sources](UPDATE-CATALOG.md)
- [Rehearsal results and fallback runs](REHEARSAL.md)
