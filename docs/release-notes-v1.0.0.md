## CSV Audit Cleaner Lite 1.0

First public freeware release for Windows 10/11 64-bit.

### Included

- Whitespace, blank-row, and duplicate cleanup
- Exact or key-column duplicate detection
- UTF-8, UTF-8 BOM, and CP949 input support
- HTML audit report, JSON summary, and JSONL run log
- Original-safe output: source CSV files are not overwritten
- Local-only operation through a temporary `127.0.0.1` address

Lite processes up to 100 data rows per CSV. The header row is not counted.

### See the actual workflow

- [Watch the actual 51-second packaged Windows workflow](https://www.youtube.com/watch?v=h8MerbgmRRY)
- [Open the actual HTML sample report](https://oneeyeview-automation.vercel.app/csv-cleaner-sample-report.html)
- [Share a verified result or report a problem](https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/issues/new?template=lite-feedback.yml)

The video and report use one fixed local sample: 4 input rows become 2 output
rows after 1 blank row and 1 duplicate are removed, with 0 failed files. They
show the workflow and evidence format; they do not promise the same counts for
every CSV.

### Verification

- ZIP size: 11,174,017 bytes
- SHA-256: `454E5027D3423A792E47B7297AC07C5371D7AAE4486008F3A964A71BEB1D39B1`
- 32 automated checks passed
- Windows launch and 101-row rejection path checked
- Included Python launcher Authenticode signature: valid

Extract the complete ZIP before running `CSV_Audit_Cleaner_Lite.exe`.
