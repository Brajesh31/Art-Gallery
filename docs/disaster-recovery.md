# ♻️ Backup, recovery, and rollback

## Current recovery model

The source of truth is the Git repository. Static hosting should be reproducible from a known commit. There is no application database to restore in the current project.

## Recovery scenarios

| Scenario | Recovery approach |
|---|---|
| Accidental source edit | Revert the offending commit or restore the file from Git history |
| Deleted image asset | Restore the original tracked asset and verify references |
| Broken deployment | Redeploy the last known-good commit |
| Compromised repository access | Revoke unauthorized access, secure the account, audit commits and workflow changes |
| External CDN outage | Wait for provider recovery or use an approved alternative after testing |
| Widget provider outage | Show a clear fallback or remove the broken widget after review |

## Rollback procedure

1. Identify the last known-good commit.
2. Confirm the affected files and user-visible impact.
3. Revert the change using Git history.
4. Run the repository quality workflow.
5. Preview all three pages.
6. Redeploy the corrected revision.
7. Verify direct page access, images, and external resources.
8. Record the incident and preventive action.

## Backup expectations

Git history protects tracked source and assets, but it is not a substitute for maintaining independent copies of original artwork and licensing records. Keep source originals and permission records in an appropriate location with access controls.

## Recovery limitations

A rollback cannot restore a third-party CDN, widget account, or external service that has been deleted or compromised. Those providers require their own recovery process.
