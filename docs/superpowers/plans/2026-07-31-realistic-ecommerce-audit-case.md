# Realistic Ecommerce Audit Case Implementation Plan

> **실행 에이전트용:** 이 계획은 짧고 기존 실행 상태와 강하게 연결되므로 implementation-planning의 인라인 executing-plans 절차로 실행한다. 스텝은 체크박스(`- [ ]`)로 추적한다.

**Goal:** Publish a reproducible 100-row ecommerce CSV audit case using the existing cleaner without changing product code.

**Architecture:** A committed deterministic input fixture is processed by the existing CLI in `automation_demo`. Only the resulting input, cleaned output, machine summary, case explanation, and root README link are added to the public distribution repository.

**Tech Stack:** Python 3.12, existing `csv_audit_cleaner` CLI, CSV, JSON, Markdown, pytest

## Global Constraints

- Use only synthetic data.
- Keep exactly 100 input data rows: 90 unique, five duplicate SKU rows, five blank rows.
- Expected output is 90 rows, five blank removals, five duplicate removals, zero failures.
- Do not modify cleaner source or claim semantic validation.
- Do not record publication as revenue.

---

### Task 1: Build and verify the public case

**Files:**
- Create: `examples/ecommerce-catalog-audit/catalog_input.csv`
- Create: `examples/ecommerce-catalog-audit/catalog_input_cleaned.csv`
- Create: `examples/ecommerce-catalog-audit/summary.json`
- Create: `examples/ecommerce-catalog-audit/README.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: `python -m csv_audit_cleaner.cli run --output <dir> --key-columns sku <input>` from `automation_demo/src`.
- Produces: a public case with exact 100-to-90 row evidence and the input hash-preservation result.

- [x] **Step 1: Create the deterministic input fixture**

Create 90 unique `SKU-001` through `SKU-090` rows, append duplicate rows for
`SKU-010`, `SKU-020`, `SKU-030`, `SKU-040`, and `SKU-050`, and append five blank rows.

- [x] **Step 2: Execute the existing cleaner**

Run from `automation_demo`:

```powershell
$env:PYTHONPATH = "src"
python -m csv_audit_cleaner.cli run --output <temporary-output> --key-columns sku <catalog_input.csv>
```

Expected: `RUN_COMPLETE succeeded=1 failed=0` and exit code `0`.

- [x] **Step 3: Add verified outputs and report**

Copy the generated cleaned CSV and summary values into the public case directory.
Write `README.md` with only observed counts, hashes, the exact command, and scope limits.

- [x] **Step 4: Link the case from the root README**

Add one concise link under the results section without changing product claims.

- [x] **Step 5: Verify the case and repository**

Run:

```powershell
python -m pytest test_feedback_form.py -q
```

Expected: existing test passes.

Also parse both CSV files and `summary.json`; expect 100 input data rows, 90 output
data rows, 90 unique output SKUs, five blank rows removed, five duplicate rows removed,
zero failures, and identical input SHA-256 before and after execution.

- [x] **Step 6: Commit**

```powershell
git add README.md examples/ecommerce-catalog-audit docs/superpowers/specs/2026-07-31-realistic-ecommerce-audit-case-design.md docs/superpowers/plans/2026-07-31-realistic-ecommerce-audit-case.md
git commit -m "docs: publish realistic ecommerce audit case"
```
