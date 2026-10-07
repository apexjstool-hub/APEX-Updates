# APEX Online Updater

This repository is the public update feed for **APEX Laptop Diagnostics**.

It works with the existing APEX `.apexupdate` modular update system.

## Included starter updates

- `system` — Hardware & Storage Tabbed Section v1.3.0
- `battery` — Battery Lab v2.1.3

`latest.json` is the file APEX checks to discover the newest module versions.

## Upload to GitHub

1. Create a new **public** GitHub repository called `APEX-Updates`.
2. Upload every file and folder from this package to the repository root.
3. Replace `YOUR_GITHUB_USERNAME` in `apex-updater-config.example.json`.
4. Your feed URL will be:

`https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/APEX-Updates/main/latest.json`

## How APEX should use the feed

1. Download `latest.json`.
2. Compare each online module version with the locally installed version.
3. Show only newer compatible updates.
4. Resolve the `file` path relative to the raw repository base URL.
5. Download the `.apexupdate`.
6. Verify its SHA-256 against `sha256`.
7. Create an APEX restore point.
8. Install the package through the existing modular updater.
9. Ask the user to restart APEX.

## Add a future update

Place your new `.apexupdate` somewhere on your PC and run:

`python tools/add_update.py PATH_TO_UPDATE.apexupdate`

Example:

`python tools/add_update.py APEX-Battery-Lab-2.2.0.apexupdate`

The helper copies the file into the correct module folder, calculates SHA-256 and updates `latest.json`.

## GitHub validation

The included GitHub Actions workflow validates the update feed on every push.

It checks:
- every referenced update exists
- each `.apexupdate` is readable
- embedded module/version match `latest.json`
- SHA-256 matches
- file size matches

## Important

This repository is the **online hosting/feed side**.

Your APEX EXE still needs a small client-side online update checker that reads this feed and hands downloaded `.apexupdate` files to your existing installer.

Do not put passwords, API keys or private signing keys in this public repository.
