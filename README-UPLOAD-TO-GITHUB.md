# APEX GitHub Online Update Release

This folder is laid out for the repository used by APEX 2.51.1:

`apexjstool-hub/APEX-Updates`

## Upload

Upload the **contents of this folder** to the root of the GitHub update repository, preserving the `updates/<module>/...` paths.

The important live feed file is:

`latest.json`

APEX reads that file automatically from the `main` branch. After the commit is live, APEX 2.51.1 can discover the newer compatible module versions during its normal online update check.

## New public-readiness updates

- `report 3.0.0` — professional functional report, strict overall verdict, five report states, evidence-source traceability, correct running version and frozen SHA-256 report snapshot.
- `gauntlet 2.0.0` — decision integrity policy: 80-100 Pass, 65-79 Review, 0-64 Fail for Advanced Diagnostics.
- `settings 2.2.0` — APEX self-health, privacy-limited support snapshot, restore/cleanup actions and one-time inline getting-started guidance. It does not create a green startup update-success popup.

The feed is cumulative and also contains current Display, Keyboard, Camera/Sound, Battery and Hardware/Storage packages so the replacement feed remains self-contained.

## Before committing

Run:

`python release-tools/validate_release.py`

and, if Node.js is available:

`node release-tools/test_policies.cjs`

Both should print PASS.

## Important limitation

The APEX 2.51.1 online updater is intentionally a **module updater**. It cannot replace the Electron runtime, `main.js`, `preload.js`, native IPC/security code or the signed Windows EXE. Those items must be included in a future rebuilt APEX core release. See `NEXT-CORE-BUILD/CORE-REBUILD-REQUIRED.md`.
