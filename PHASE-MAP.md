# Public Release Phase Map

## Phase 1 — Reports and Pass / Fail
**Delivered online**

- APEX-branded professional functional report.
- Overall `PASS`, `FAIL` or `REVIEW REQUIRED` verdict.
- Separate `PASS`, `FAIL`, `REVIEW`, `NOT TESTED`, and `N/A · NOT FITTED` reporting states.
- Unsupported-but-not-confirmed-absent items become `NOT VERIFIED` and block clearance instead of silently passing.
- Verification source shown as automatic evidence or technician verified.
- Evidence count per test.
- Correct running APEX core version in exports instead of hard-coded 2.41.0.
- Frozen final report snapshot with SHA-256 digest. Exports use the frozen snapshot while locked.
- Advanced health score 65-79 no longer becomes Pass.

## Phase 2 — Reliability testing
**Delivered with the GitHub release**

- Release package/hash/manifest validator.
- Decision-policy test cases.
- Report-state classification test cases.
- Feed is compatible with the APEX 2.51.1 updater whitelist and parser.

## Phase 3 — Public security build
**Requires next rebuilt EXE; not safe to fake as a module update**

The existing module updater is not permitted to replace Electron, `main.js`, preload/IPC security code, or Windows signing. The required next-core work is documented in `NEXT-CORE-BUILD`.

## Phase 4 — First-use experience
**Delivered online, non-popup**

- One-time inline Overview guide.
- Explains local diagnostics, resolving Review / Not Tested items, and final report locking.
- It is not an update-success toast, startup overlay or green popup.

## Phase 5 — Public support
**Delivered online**

Settings gains an APEX self-maintenance/public-support panel with:

- APEX health check.
- Core/module/update/recovery status.
- Decision-policy self-test status.
- Renderer-error count.
- Privacy-limited support snapshot export.
- Create restore point.
- Clean old update files.

The support snapshot intentionally excludes device serial numbers, test results, Wi-Fi credentials and other target-laptop diagnostic evidence.
