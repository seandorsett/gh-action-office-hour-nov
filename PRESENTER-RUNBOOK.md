# Presenter runbook - November 10, 2026

## Before the session

Check billing and account entitlement. Use synthetic content only. Confirm all
selected workflows appear on the default branch. Run preparation when source
frontmatter or action dependencies change; review its generated artifact and
commit the files. Do not edit generated lockfiles by hand.

Configure Copilot authentication in GitHub Settings, run preflight, and rehearse
the agent. Keep a successful report issue and workflow run open as fallback.
No inference has been demonstrated merely because compilation succeeded.
For the secret-based path, use a fine-grained PAT with only the Copilot Requests:
Read account permission and store it as repository secret
`COPILOT_GITHUB_TOKEN`. Do not add repository-content permissions to that PAT or
paste it into Chat. Confirm the repository secret is visible before launching.

Recheck official announcements before November 10. The research window ends
November 2, not the session day.

## 0-5 minutes - Opening

Say: "Today we will make Actions dependencies reproducible, then spend most of
our time on GitHub Agentic Workflows: how a Markdown request becomes a guarded
Actions workflow, and what the live run actually does."

Explain that all demos launch on github.com, and that this session focuses
only on the two selected updates.

## 5-10 minutes - Update #1: workflow dependency lockfiles

Spend 2 minutes explaining movable action tags, transitive action dependencies,
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

## 10-50 minutes - Update #2: Agentic Workflows deep dive

Suggested pacing: 6 minutes on the problem and architecture, 6 minutes on
source and generated workflow review, 5 minutes on safeguards and permissions,
15 minutes on dispatch/run inspection, 5 minutes on the output and limitations,
and 3 minutes on adoption lessons.

Explain: Markdown instructions and frontmatter -> compile -> ordinary Actions
YAML -> read-only agent -> validated, permission-controlled safe output.

Show repo-status.md and repo-status.lock.yml. They differ from actions.lock.
Launch **Repo status office hour** from Actions.
Explain that this real workflow runs manually, reads the synthetic demo
repository, gives the agent read-only access, and allows one report issue via
a separate safe-output job. The compiled file exposes the job graph and pinned
components for review; it is not the same as the actions.lock dependency file.

While waiting, discuss permissions, network containment, safe-output limits,
authentication and AI budget. Instructions are not a security boundary by
themselves; tools and permissions matter. AI output is variable.

Show the report issue and compare its claims with repository evidence. The
agent should distinguish this private repository from public-policy scope.
Do not use production content to make the example more impressive.

Fallback: if authentication is missing, show the explicit preflight failure
and walk through source and compilation only. Label live inference unavailable,
not a completed report. If rehearsal succeeded earlier, show the saved result.

## 50-60 minutes - Q&A

Discussion prompts: Which repository tasks are suitable for bounded agents?
What should remain human-reviewed? What permissions and safe outputs would
customers permit? What signals would make this automation trustworthy?

No production policy, credential or network access changes are part of this
session. Record follow-up actions in GitHub rather than changing them live.
