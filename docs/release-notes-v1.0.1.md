## CSV Audit Cleaner Lite 1.0.1

Small usability update for the free Windows 10/11 64-bit edition.

### Changed

- Replaced the easy-to-miss full-version text link with a clear upgrade card.
- The card states the 100-row threshold, the $15 one-time price, and that the
  full edition keeps the same workflow.
- Preserved the local-only workflow, 100-row Lite limit, output format, and
  source-safe behavior.

### See the actual workflow

- [Watch the actual 51-second packaged Windows workflow](https://www.youtube.com/watch?v=h8MerbgmRRY)
- [Open the actual HTML sample report](https://oneeyeview-automation.vercel.app/csv-cleaner-sample-report.html)
- [Share a verified result or report a problem](https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/issues/new?template=lite-feedback.yml)

The video and report use one fixed local sample: 4 input rows become 2 output
rows after 1 blank row and 1 duplicate are removed, with 0 failed files. They
show the workflow and evidence format; they do not promise the same counts for
every CSV.

### Verification

- Asset: `CSV_Audit_Cleaner_Lite_v1.0.1.zip`
- ZIP size: 11,174,177 bytes
- SHA-256: `7787166796EDFB71C892CCDB2DE0A437FA046E9D2C9A66B2EE831AD427D6B21C`
- 40 automated checks passed
- Windows launch, new upgrade card, and 101-row rejection path checked
- Included Python launcher Authenticode signature: valid

Extract the complete ZIP before running `CSV_Audit_Cleaner_Lite.exe`.
