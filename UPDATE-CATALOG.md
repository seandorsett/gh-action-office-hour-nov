# DXC GitHub Actions Office Hour - November 10, 2026

Research snapshot: November 2, 2026.
Window: October 4-November 2, 2026, inclusive (30 calendar dates).
This is not a forecast of announcements between November 3 and the session.

Session constraint: 50 minutes presentation and demos, followed by 10 minutes Q&A.
Selected topics: 1, 2, 3, 5 and 6. Demo feasibility below is an assessment,
not evidence of an implemented or successfully executed demo.

## Topic selection

| ID | Update and announcement date | Demo feasibility from github.com | Proposed demonstration | Prerequisites and limitations | Suggested segment |
|---|---|---|---|---|---|
| 1 | Workflow dependency lockfiles GA, October 28; preview October 14 | Yes - strong workflow demo | Run an onboarded workflow, inspect actions.lock and the resolved action commits, then show a controlled missing-dependency failure and regeneration through a preparation workflow. | Generate with gh actions-lock, never hand-edit. Commit generated files before execution. Lockfiles do not pin job-level reusable workflow references, runner images, or all build inputs. Policy enforcement needs administrator access. | 12 minutes |
| 2 | GitHub Agentic Workflows GA, October 28 | Yes - conditional on inference authentication and billing | Manually dispatch a repository-status agent, inspect its Markdown source and compiled Actions YAML, and show its report in GitHub. | Requires an approved AI engine and authentication. Default Copilot engine requires a Copilot license; organization billing has additional subscription requirements. Precompile and commit workflow files. Use synthetic repository content, read-only access and limited safe outputs. AI credits and Actions usage may apply; latency and output vary. | 15 minutes |
| 3 | pull_request_target default blocking enforcement rescheduled, November 2 | Partly - safe event demonstration and policy UI; not a natural enforcement demo on session day | Compare harmless pull_request and pull_request_target event metadata, then inspect policy configuration or insights. Never check out or execute fork code in the privileged target context. | Applies to public repositories, not private/internal repositories or GHES. Permanent enforcement December 2. Brownouts November 9 and 16, 16:00-18:00 UTC. November 10 is the day after the first brownout; do not promise a default-block failure then. This private demo repository is not affected by the public-repository default. Configuring a separate active policy requires administrator access and explicit approval. | 8 minutes |
| 4 | Xcode 27 runner image GA, October 15 | Yes - conditional on runner availability and budget | Dispatch an xcode-27 job, display Xcode/SDK versions and arm64 architecture, and build/test a tiny Swift package. | Apple Silicon only. Labels are xcode-27 and xcode-27-xlarge. Check repository entitlement, quota and billing before selection; do not assume xlarge is free. | 8 minutes |
| 5 | Multi-cloud GitHub-hosted compute, October 28 | Partial - readiness workflow, not proof of failover | Run an eligible Linux job and inspect the published Actions IP ranges with a network-readiness summary. | Eligible standard 2/4-core Linux and compatible larger runners only. Enterprise Cloud customers opt in; Free/Pro/Team automatic. Scheduling chooses the provider, so a workflow cannot guarantee AWS placement, force failover or prove improved reliability. Windows and specialized/private-network configurations excluded. | 4 minutes |
| 6 | Actions blob-storage endpoints added to Meta API, October 22 | Partial - API and job-summary demonstration | Fetch current Meta API data and publish a job summary for allowlist review. | New inclusive host ranges: productionresultssa30-49 and productionresultssa100-199 under blob.core.windows.net. A hosted job does not prove a corporate firewall is configured correctly or uses a particular new host. Pair with topic 5. | 3 minutes |
| 7 | Actions runner v2.338.0 October 6; v2.338.1 prerelease October 22; v2.338.2 October 26 | Limited - mostly operational briefing | Inspect the runner version shown in job setup and explain internal Node 24 use and connectivity probes. | Progressive rollout; a GitHub-hosted workflow cannot control runner version or demonstrate self-hosted service internals. Internal Node 24 is not the same as the application Node version selected by setup-node. Release notes also list self-repository action manifest references; do not promise a live demo without further verification. | 3 minutes |

Suggested selection: 1, 2, 3, 5 and 6.
Suggested agenda: opening 4 minutes; lockfiles 12; agentic workflows 15;
security policy update 8; combined network readiness 7; takeaways/buffer 4;
Q&A 10. Total: 60 minutes.

An alternative without AI inference uses topics 1, 3, 4, 5 and 6, with the
remaining time allocated to deeper lockfile and policy walkthroughs.

## Demo delivery requirements

- Launch presentation demos through Actions > Run workflow, or a documented GitHub event.
- Keep workflow sources, generated lockfiles, instructions and results in GitHub.
- Run compilation/preparation in GitHub-hosted workflows where practical, with
  reviewed generated outputs committed before the presentation.
- No local runner or presenter terminal should be necessary during delivery.
- Use a dedicated demo repository with synthetic data, least-privilege
  permissions, explicit timeouts and no production deployment.
- Rehearse selected demos and retain successful run links and outputs as fallbacks.
- Review plan restrictions, organization policies and any paid usage before execution.
- Recheck availability and announcements before November 10; this snapshot
  does not include future releases.

## Presentation requirements

Use a suitable original design: high-contrast dark backgrounds, purple accents,
and readable workflow examples. The user has no template and approved choosing
a suitable design. Include speaker notes, demo cues, timing, prerequisites,
source references, fallback instructions, and a final 10-minute Q&A section.

Target repository: https://github.com/seandorsett/gh-action-office-hour-nov
Created as private with the user's approval. Selected workflow sources,
generated lockfiles and presenter materials are published. See REHEARSAL.md
for observed execution outcomes and PRESENTATION.md for the generated deck.

## Primary sources

1. Lockfiles GA: https://github.blog/changelog/2026-10-28-github-actions-workflow-lockfiles-are-generally-available/
2. Lockfiles preview: https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview/
3. Lockfile behavior: https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles
4. Workflow policies: https://docs.github.com/en/actions/how-tos/administer/control-workflow-execution
5. Agentic Workflows GA: https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/
6. Agentic quickstart and authentication: https://github.github.com/gh-aw/setup/quick-start/
7. Default trigger policy and dates: https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/
8. Xcode image GA: https://github.blog/changelog/2026-10-15-xcode-27-runner-image-generally-available/
9. Multi-cloud compute: https://github.blog/changelog/2026-10-28-github-actions-adds-multi-cloud-compute-to-improve-reliability/
10. Blob endpoints: https://github.blog/changelog/2026-10-22-meta-api-endpoints-updated-for-actions-blob-storage/
11. Runner releases: https://github.com/actions/runner/releases
12. Runner v2.338.0: https://github.com/actions/runner/releases/tag/v2.338.0
13. Runner v2.338.2: https://github.com/actions/runner/releases/tag/v2.338.2

Official changelog monthly indexes and runner release publication timestamps
were reviewed. Broader Copilot and security announcements were excluded unless
directly relevant to Actions. Preview and GA announcements for lockfiles are
counted as one topic, not two features.
