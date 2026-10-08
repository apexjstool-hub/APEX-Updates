# Report v3.1.2 visibility fix (not yet published)

Requested behaviour: omit **untested** touchscreen, stability and other diagnostic rows from the displayed report and PDF. Do not label a missing touchscreen as tested or verified unsupported. Preserve actual PASS, FAIL, REVIEW and NOT VERIFIED results, and do not mark a blank report PASS.

This is an **unpublished build preparation**. Live `latest.json` still advertises report **3.1.1**.

On a checked-out copy of this repository run:

```sh
python release-tools/build_report_visibility_update.py
```

This builds `updates/report/APEX-report-3.1.2.apexupdate` using **the live report 3.1.1 package as input**, preserving its PDF fixes. Inspect the output and test an installed APEX application before updating `latest.json` with the displayed filename, SHA-256 and byte size.

Important: frozen report snapshots remain frozen. Unlock and relock an old report if you want a newly captured result set.
