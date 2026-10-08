# APEX update repository — safe maintenance

**Live repository:** https://github.com/apexjstool-hub/APEX-Updates

## Do not break the updater

APEX uses the raw GitHub URL `https://raw.githubusercontent.com/apexjstool-hub/APEX-Updates/main/latest.json` to check for modular updates. Each `modules.*.file` entry currently resolves relative to the same raw repository base. **Keep `latest.json` in the root and preserve the paths of every update it references.**

Do not simply move `*.apexupdate` files from the root into `updates/` or GitHub Releases: existing APEX builds might still request the old raw URLs. Changing hosting locations requires a separately tested compatibility change to the client and manifest. The same applies to any older release or URL which may have been distributed.

## Publishing a module update

1. Create and test the `.apexupdate` on a test device.
2. Keep existing package URLs live. Add the new package to the repository at the path you intend to advertise.
3. Update only the relevant entry in `latest.json`: `version`, `file`, `sha256`, `sizeBytes`, and the supported `minCoreVersion`.
4. Verify the referenced download URL resolves and its byte size and SHA-256 match.
5. Verify APEX discovers, downloads, validates, restores, and installs the test update. Test the restart and rollback paths.
6. Publish only when these checks pass. Do not delete existing packages as part of the same release.

### Future cleanup

* Keep the root manifest and all existing package download URLs intact for compatibility.
* Use `updates/<module>/` for new packages only **after** checking that your installed updater accepts slash-separated relative paths.
* Consider GitHub Releases for core EXE downloads. The current `latest.json` declares core `updateType: manual`, so this change does not automatically create EXE updates.
* Existing update packages can be archived or moved only after a compatibility audit. Git history alone does not guarantee that old raw file URLs remain valid.
* Use `.gitignore` to prevent generated build artifacts from being added on future commits. It does not untrack files already committed.

## Current compatibility note (8 October 2026)

The update feed advertises APEX core 2.51.1 with modular packages in the repository root. The feed is a live interface, not merely a file listing. Updating the layout should not interrupt it.
