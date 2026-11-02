# Presenter runbook - November 10, 2026

## Before the session

Check billing and account entitlement. Use synthetic content only. Confirm all
selected workflows appear on the default branch. Run preparation when source
frontmatter or action dependencies change; review its generated artifact and
commit the files. Do not edit generated lockfiles by hand.

Configure Copilot authentication in GitHub Settings, run preflight, and rehearse
the agent. Keep a successful report issue and workflow run open as fallback.
No inference has been demonstrated merely because compilation succeeded.

Recheck official announcements before November 10. The research window ends
November 2, not the session day.

## 0-4 minutes - Opening

Say: "Today we will make automation more reproducible, add bounded AI automation,
and prepare for the security and network changes announced this month."

Explain that all demos launch on github.com. Distinguish generally available
features from upcoming enforcement and infrastructure rollouts.

## 4-16 minutes - Workflow dependency lockfiles

Spend 4 minutes explaining movable action tags, transitive action dependencies,
and readable workflow references. Show the committed actions.lock in Code.

Launch **01 - Workflow dependency lockfiles**. While it runs, explain:
"The locked action commit is the code that runs. The lockfile is an inventory
and integrity mechanism, not proof that the dependency itself is safe."

Show verification and controlled temporary drift being rejected. Be explicit:
"This negative case is the CLI coverage verifier. We have not enabled an
organization policy or deliberately broken the default branch."

Mention gradual onboarding and Dependabot lockfile regeneration. Reusable
workflow references at job level need full-SHA pinning; lockfiles do not freeze
all build inputs. Require-lockfile policy needs admin planning.

Fallback: committed lockfile and saved successful run. Do not manufacture
success if the extension or feature is unavailable.

## 16-31 minutes - Agentic Workflows

Explain: Markdown instructions and frontmatter -> compile -> ordinary Actions
YAML -> read-only agent -> validated, permission-controlled safe output.

Show repo-status.md and repo-status.lock.yml. They differ from actions.lock.
Launch **Repo status office hour** from Actions.

While waiting, discuss permissions, network containment, safe-output limits,
authentication and AI budget. Instructions are not a security boundary by
themselves; tools and permissions matter. AI output is variable.

Show the report issue and compare its claims with repository evidence. The
agent should distinguish this private repository from public-policy scope.
Do not use production content to make the example more impressive.

Fallback: if authentication is missing, show the explicit preflight failure
and walk through source and compilation only. Label live inference unavailable,
not a completed report. If rehearsal succeeded earlier, show the saved result.

## 31-39 minutes - Safe events and enforcement timing

Say: "The first public-repository brownout was scheduled for yesterday,
November 9, 16:00-18:00 UTC. The next is November 16. Permanent enforcement
is December 2, not November 2." Do not assert outcomes without evidence.

Launch **03 - Safe event context** manually. Point out it is a manual event,
not a simulated pull request. For a real comparison, use GitHub's file editor
to create a harmless README-only branch and open a PR through the web UI.
Inspect both pull_request and pull_request_target runs and their refs/SHAs.

The target workflow checks out nothing, has no custom secrets or write access,
and never runs PR-supplied code. Do not add a head checkout to "make it real."

Show the official policy page. Public default blocking is not enforced by this
private repository. Do not change visibility or policy during the presentation.
For policy insights, use a separately authorized eligible repository if available;
otherwise show documentation and explain scope.

Fallback: source and manual metadata. Never describe a private-repository run
as proof of the public default block.

## 39-46 minutes - Network readiness

Launch **04 - Multi-cloud and blob readiness**.

Say: "GitHub chooses provider placement. This workflow is a readiness aid,
not a cloud-provider selector, failover test or benchmark."

Show Meta API data and summary. Explain why Azure-only IP assumptions can break
eligible hosted jobs. Enterprise Cloud customers opt in; specialized and
private-network runners are excluded from this announcement.

Explain inclusive blob host-number ranges 30-49 and 100-199, and that successful
summary publication only demonstrates this runner's connectivity. Do not apply
these illustrative range strings directly as firewall rules.

Fallback: saved summary and official API/announcement links.

## 46-50 minutes - Close

Ask participants to inventory actions, select a lockfile pilot, choose one
bounded agent task, review privileged PR triggers, and involve network owners.
Use remaining time as buffer; stop new demos at minute 50.

## 50-60 minutes - Q&A

Discussion prompts: Which workflows should adopt lockfiles first? Which tasks
are suitable for bounded agents? Who owns event-policy rollout? How are runner
IP and storage endpoint changes reviewed?

No production policy, credential or network access changes are part of this
session. Record follow-up actions in GitHub rather than changing them live.
