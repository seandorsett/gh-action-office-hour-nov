# GitHub Actions November Updates

DXC Office Hour: **November 10, 2026**.

[Open GitHub Actions November Updates.pptx](https://microsoft-my.sharepoint.com/personal/sedorset_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B4D198BF3-CC7D-4230-A2BF-A4420EAEF6F3%7D&file=GitHub%20Actions%20November%20Updates.pptx&action=edit&mobileredirect=true)

The Office-generated deck was revamped to cover only update #1 (workflow
dependency lockfiles) and update #2 (GitHub Agentic Workflows), with speaker
notes. The requested agenda is 5 minutes on #1, 40 minutes for a deep dive
on #2, and the original 10 minutes of Q&A; the opening occupies the remaining
5 minutes of the 60-minute session.

Style chosen in PowerPoint: **Dark Canvas Purple Accents**.

## Persistence

The repository includes a copy at
[slides/GitHub Actions November Updates.pptx](slides/GitHub%20Actions%20November%20Updates.pptx),
alongside the canonical Microsoft 365 link above. The archived copy is
Office-encrypted; opening it may require Microsoft 365 authorization. GitHub
access alone does not grant access to the protected presentation.

The repository is private. Keep the SharePoint-hosted presentation as the
editable canonical version and update the repository copy when it changes.

## Delivery cautions

- Research window: October 4-November 2, 2026, not future announcements.
- The Agentic Workflows source and compiled workflow are committed in GitHub.
- GitHub confirms the repository secret name `COPILOT_GITHUB_TOKEN` is present;
  its value was not accessed. Preflight passed and live inference succeeded on
  November 5, 2026: [preflight](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/42130203122),
  [Agentic Workflow run](https://github.com/seandorsett/gh-action-office-hour-nov/actions/runs/42130308648),
  and [generated report issue #2](https://github.com/seandorsett/gh-action-office-hour-nov/issues/2).
- Live runs depend on a valid credential, Copilot entitlement and available
  budget; check those again before the November 10 session.
- Use [the runbook](PRESENTER-RUNBOOK.md) for precise commands, caveats and
  fallback handling. Use [rehearsal evidence](REHEARSAL.md) for observed runs.
