# Realistic Ecommerce Audit Case Design

## Goal

Replace the tiny four-row proof as the strongest public evidence with a deterministic,
self-produced 100-row ecommerce catalog audit that a buyer can inspect before paying.

## Chosen approach

Commit one synthetic UTF-8 CSV with exactly 100 data rows: 90 unique product rows,
five duplicate SKU rows, and five completely blank rows. Run the existing CSV Audit
Cleaner with `sku` as the duplicate key, then publish the unchanged input, cleaned
output, machine summary, and a concise case report.

This is preferred over reusing the four-row fixture because it better represents an
operational file, and over an external dataset because it has no licensing or customer
privacy dependency.

## Scope

- No cleaner source-code or product behavior changes.
- No external or customer data.
- No claims beyond whitespace trimming, blank-row removal, SKU-key deduplication,
  row counts, and source-file hash preservation.
- The expected result is 100 input rows to 90 output rows, with five blanks and five
  duplicate SKU rows removed and zero failed files.

## Public artifacts

- `examples/ecommerce-catalog-audit/catalog_input.csv`
- `examples/ecommerce-catalog-audit/catalog_cleaned.csv`
- `examples/ecommerce-catalog-audit/summary.json`
- `examples/ecommerce-catalog-audit/README.md`
- Root `README.md` gains one link to the case.

## Verification

Run the existing CLI from the sibling `automation_demo` source with `sku` as the key.
Confirm the summary values, compare the input SHA-256 before and after, check that the
output contains 90 unique SKUs, and rerun the distribution repository's existing test.

## Non-goals

This case does not prove Excel, PDF, semantic field validation, CAPTCHA bypass,
unauthorized collection, or a customer sale. Publication is distribution evidence,
not revenue.
