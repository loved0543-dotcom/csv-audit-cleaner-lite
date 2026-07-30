# CSV Lite Feedback Form Implementation Plan

> **실행 에이전트용:** 이 계획은 implementation-planning의 executing-plans
> 절차로 인라인 실행한다. 스텝은 체크박스(`- [ ]`)로 추적한다.

**Goal:** 무료 Lite 실제 사용자가 민감정보 없이 성공·문제·질문을 공개 근거로
남길 수 있는 GitHub Issue Form을 제공한다.

**Architecture:** `.github/ISSUE_TEMPLATE/lite-feedback.yml`을 공개 입력 seam으로
둔다. `test_feedback_form.py`가 YAML 계약과 README·Release 발견 경로를 검증하고,
기존 v1.0.0 Release 설명은 정본 파일에서 다시 적용한다.

**Tech Stack:** GitHub Issue Forms YAML, Python 3, PyYAML 6.0.3, GitHub CLI

## Global Constraints

- Issue Form 1개만 추가한다.
- CSV 원본·고객정보·이메일·로컬 경로·민감 보고서 업로드를 금지한다.
- 이메일·지원 SLA·환불·맞춤 지원·후기 보상을 약속하지 않는다.
- 기능·가격·Lite ZIP·릴리스 태그·크기·SHA-256을 바꾸지 않는다.
- 실제 제3자 제출 전에는 후기나 사용 사례가 생겼다고 말하지 않는다.
- 공개 seam은 Issue Form URL, README 링크, v1.0.0 Release 링크다.
- 짧은 단일 저장소 변경이라 인라인 실행한다.

---

### Task 1: Issue Form 계약

**Files:**
- Create: `test_feedback_form.py`
- Create: `.github/ISSUE_TEMPLATE/lite-feedback.yml`

**Interfaces:**
- Consumes: 사용 유형, 버전, 관찰 결과, 선택 수치, 개인정보 금지 확인
- Produces: GitHub가 렌더할 수 있는 `CSV Audit Cleaner Lite feedback` Issue Form

- [x] **Step 1: 실패하는 공개 seam 검사 작성**

```python
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "lite-feedback.yml"


def test_feedback_form_contract():
    data = yaml.safe_load(FORM.read_text(encoding="utf-8"))
    assert data["name"] == "CSV Audit Cleaner Lite feedback"
    assert data["title"] == "[Lite feedback] "

    ids = {item.get("id") for item in data["body"] if item.get("id")}
    assert {"outcome", "version", "observation", "counts", "privacy"} <= ids

    privacy = next(item for item in data["body"] if item.get("id") == "privacy")
    assert privacy["type"] == "checkboxes"
    assert privacy["attributes"]["options"][0]["required"] is True
    label = privacy["attributes"]["options"][0]["label"]
    for forbidden in ("CSV files", "customer data", "email addresses", "local paths"):
        assert forbidden in label
```

- [x] **Step 2: 검사 실행해 RED 확인**

Run: `python -m unittest test_feedback_form.py -v`

Expected: ERROR because `lite-feedback.yml` does not exist.

- [x] **Step 3: 최소 Issue Form 작성**

유형 dropdown, v1.0.0 버전, 필수 observation, 선택 counts, 필수 개인정보
확인란을 정확히 한 번씩 만든다.

- [x] **Step 4: 검사 실행해 GREEN 확인**

Run: `python -m unittest test_feedback_form.py -v`

Expected: `1 test` PASS.

### Task 2: README·Release 발견 경로

**Files:**
- Modify: `test_feedback_form.py`
- Modify: `README.md`
- Modify: `docs/release-notes-v1.0.0.md`

**Interfaces:**
- Consumes: `https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/issues/new?template=lite-feedback.yml`
- Produces: README와 기존 v1.0.0 Release의 동일한 공개 피드백 링크

- [x] **Step 1: 링크 계약 검사 추가**

```python
def test_feedback_link_is_discoverable_without_changing_artifact():
    feedback_url = (
        "https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/"
        "issues/new?template=lite-feedback.yml"
    )
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    release = (ROOT / "docs" / "release-notes-v1.0.0.md").read_text(
        encoding="utf-8"
    )

    assert readme.count(feedback_url) == 1
    assert release.count(feedback_url) == 1
    for text in (readme, release):
        assert "11,174,017 bytes" in text
        assert (
            "454E5027D3423A792E47B7297AC07C5371D7AAE4486008F3A964A71BEB1D39B1"
            in text
        )
```

- [x] **Step 2: 검사 실행해 RED 확인**

Run: `python -m unittest test_feedback_form.py -v`

Expected: link test FAIL because README and Release contain 0 links.

- [x] **Step 3: 두 안내 표면에 동일 링크 1회 추가**

문구는 `Share a verified result or report a problem`으로 통일한다. 후기·보상·
지원 약속은 추가하지 않는다.

- [x] **Step 4: 전체 검사 실행해 GREEN 확인**

Run: `python -m unittest test_feedback_form.py -v`

Expected: `2 tests` PASS.

### Task 3: 공개·실제 폼 검증

**Files:**
- Modify: `docs/superpowers/plans/2026-07-31-csv-lite-feedback-form.md`

**Interfaces:**
- Consumes: 검증된 Issue Form과 링크
- Produces: 공개 GitHub 폼·README·Release와 실행 증거

- [x] **Step 1: diff 자체 검수와 커밋**

Run:

```powershell
git diff --check
git add .github README.md docs test_feedback_form.py
git commit -m "feat: add privacy-safe Lite feedback form"
```

Expected: Issue Form·테스트·두 링크만 포함한 커밋.

- [x] **Step 2: push하고 폼 URL 검증**

Run:

```powershell
git push origin HEAD
```

Expected: raw 템플릿과 README가 HTTP `200`이고, 제출 URL은 로그인 사용자에게
폼을 제공한다.

- [x] **Step 3: 기존 v1.0.0 Release 설명 재적용**

Run:

```powershell
gh release edit v1.0.0 `
  --repo loved0543-dotcom/csv-audit-cleaner-lite `
  --notes-file docs/release-notes-v1.0.0.md
```

Expected: 같은 URL·태그·자산 유지.

- [x] **Step 4: 공개 완료 검사와 기록**

README·Release 링크 각 1회, 폼 필드, Release 자산 1개·크기·digest, 실제 이슈
0건을 확인한다. 제출이 없으므로 제3자 후기 `0`을 유지한다.

## 실행 결과 — 2026-07-31 06:58 KST

- RED: 폼 파일 부재, 이후 README·Release 링크 0회로 각 계약 검사가 실패했다.
- GREEN: `python -m unittest test_feedback_form.py -v`에서 2개 검사 통과.
- 공개 커밋: `139090c992acc369d5a8d0391f69e4f430624563`
- raw 폼과 README HTTP `200`; README 피드백 링크 정확히 1회.
- 비로그인 제출 URL은 GitHub 로그인으로 이동한다. 익명 제출 가능이라고
  주장하지 않는다.
- 기존 v1.0.0 Release는 같은 태그·이름·자산 1개를 유지했다.
- ZIP `11,174,017`바이트, SHA-256 digest 불변, 표시 다운로드 `2`.
- 공개 이슈 `0`; 실제 제3자 후기·사용 사례 `0`.
