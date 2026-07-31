<p align="center">
  <img src="assets/cover.png" alt="CSV Audit Cleaner product cover" width="100%">
</p>

# CSV Audit Cleaner Lite

Clean CSV whitespace, blank rows, and duplicates on a Windows PC, then keep an
HTML audit report and machine-readable run logs. Files stay on the computer;
the app does not upload CSV data to a cloud service.

[Download the free Lite release](https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/releases/download/v1.0.1/CSV_Audit_Cleaner_Lite_v1.0.1.zip)
·
[Get the unlimited $15 version](https://lovelife717.gumroad.com/l/csv-audit-cleaner)
·
[View product details](https://oneeyeview-automation.vercel.app)

[Watch the actual 51-second packaged Windows workflow](https://www.youtube.com/watch?v=h8MerbgmRRY)
·
[Open the actual HTML sample report](https://oneeyeview-automation.vercel.app/csv-cleaner-sample-report.html)
·
[Share a verified result or report a problem](https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/issues/new?template=lite-feedback.yml)

Need batch processing and the full audit workflow? [Get CSV Audit Cleaner for $15](https://lovelife717.gumroad.com/l/csv-audit-cleaner).

Need data collected from one source you are authorized to use? [Review the fixed $149 Data Reliability Pilot](https://oneeyeview-automation.vercel.app/data-reliability-pilot):
up to 500 records with 24-hour delivery and explicit evidence and exclusion
boundaries.

The video and report use one fixed local sample: 4 input rows become 2 output
rows after 1 blank row and 1 duplicate are removed, with 0 failed files. They
show the workflow and evidence format; they do not promise the same counts for
every CSV.

## What it does

- Trims leading and trailing whitespace.
- Removes fully blank rows.
- Removes exact duplicates or duplicates based on chosen key columns.
- Writes cleaned UTF-8 BOM CSV files without overwriting the originals.
- Produces an HTML audit report, JSON summary, and JSONL run log.
- Reads UTF-8, UTF-8 BOM, and CP949 CSV files.
- Runs through a temporary `127.0.0.1` address on the same PC.

<p align="center">
  <img src="assets/app.png" alt="CSV Audit Cleaner Lite application screen" width="900">
</p>

## Lite and full editions

| | Lite | Full |
|---|---:|---:|
| Price | Free | $15 one-time |
| Rows per CSV | Up to 100 data rows | Unlimited by edition |
| Batch size | Up to 100 MB per run | Up to 100 MB per run |
| HTML audit report | Yes | Yes |
| JSON and JSONL evidence | Yes | Yes |
| Cloud upload or telemetry | No | No |

The header row is not counted toward the Lite limit. The limit is checked
before a cleaned output file is written.

## Quick start

1. Download `CSV_Audit_Cleaner_Lite_v1.0.1.zip` from the release page.
2. Extract the complete ZIP into a new folder.
3. Double-click `CSV_Audit_Cleaner_Lite.exe`.
4. Add one or more CSV files and optionally enter duplicate-key columns.
5. Select **Clean & verify**, then inspect the generated report.
6. Select **Exit app** when finished.

Windows 10/11 64-bit is required. No installation, Python setup, cloud account,
subscription, paid API, or administrator access is required.

## Verify the download

Release file:

```text
CSV_Audit_Cleaner_Lite_v1.0.1.zip
11,174,177 bytes
SHA-256 7787166796EDFB71C892CCDB2DE0A437FA046E9D2C9A66B2EE831AD427D6B21C
```

PowerShell verification:

```powershell
Get-FileHash .\CSV_Audit_Cleaner_Lite_v1.0.1.zip -Algorithm SHA256
```

The release was checked with 40 automated tests and a real Windows launch,
including the 101-row rejection path. The included Python launcher has a valid
Python Software Foundation Authenticode signature.

## Scope

This edition does not edit Excel workbooks, PDFs, images, or values using AI.
It does not automate browser logins or bypass CAPTCHAs. Keep backups and verify
results before using cleaned files in production.

Copyright (c) 2026 One Eye Automation. See [LICENSE.txt](LICENSE.txt).
