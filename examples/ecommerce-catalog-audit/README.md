# 100-row ecommerce catalog audit

This is a self-produced synthetic fixture. It contains no customer, marketplace, or
personal data.

## Observed result

| Check | Result |
|---|---:|
| Input data rows | 100 |
| Output data rows | 90 |
| Completely blank rows removed | 5 |
| Duplicate SKU rows removed | 5 |
| Failed files | 0 |
| Unique output SKUs | 90 |
| Input SHA-256 before and after | identical |

Input SHA-256:
`f83921fc09c6d72d1f4b674768d7deb0d49b9966d73183bcf28ce011f03fda3c`

The five duplicate rows use `SKU-010`, `SKU-020`, `SKU-030`, `SKU-040`,
and `SKU-050`. The cleaner was run with `sku` as the duplicate key, so the
first occurrence was preserved. Five fully empty rows were removed. Leading and
trailing spaces in cells were trimmed.

## Command

From the sibling source workspace:

```powershell
$env:PYTHONPATH = "src"
python -m csv_audit_cleaner.cli run \
  --output ..\_artifacts\ecommerce_case_20260731 \
  --key-columns sku \
  ..\distribution\csv-audit-cleaner-lite\examples\ecommerce-catalog-audit\catalog_input.csv
```

Observed exit code: `0`.

## Files

- [Original synthetic input](./catalog_input.csv)
- [Cleaned output](./catalog_input_cleaned.csv)
- [Machine summary](./summary.json)

## Scope boundary

This case proves whitespace trimming, blank-row removal, duplicate detection by
an explicit SKU key, row-count reporting, failure count, and preservation of the
input file hash. It does not prove Excel or PDF support, semantic field
validation, CAPTCHA bypass, unauthorized collection, or customer revenue.

