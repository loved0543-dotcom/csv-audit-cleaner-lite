# CSV Lite README Proof Links Implementation Plan

> **실행 에이전트용:** 이 계획을 태스크 단위로 구현할 때
> implementation-planning의 executing-plans 절차를 쓴다. 스텝은
> 체크박스(`- [ ]`) 문법으로 추적한다.

**Goal:** 무료 Lite 저장소 README에서 실제 영상·샘플 보고서·32개 검사 근거를
즉시 확인하게 한다.

**Architecture:** 전달 ZIP과 릴리스는 그대로 두고 사용자 진입점인 `README.md`
한 파일만 수정한다. 정적 계약 검사와 공개 HTTP·GitHub 렌더 확인으로 검증한다.

**Tech Stack:** GitHub Markdown, PowerShell, Git

## Global Constraints

- 기능·릴리스 태그·ZIP URL·크기·SHA-256을 바꾸지 않는다.
- 고정 로컬 표본이며 모든 CSV에 같은 결과를 보장하지 않는다고 밝힌다.
- 새 지원·할인·환불·업데이트 약속을 만들지 않는다.
- 짧고 강한 세션 연속성이 필요한 단일 문서 수정이므로 인라인 실행한다.

---

### Task 1: README 증거 링크와 검사 수 정합성

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: 공개 YouTube ID `h8MerbgmRRY`, 공개 샘플 보고서 URL, 판매본 검사 수 `32`
- Produces: 무료판 방문자가 직접 검증 가능한 GitHub README

- [x] **Step 1: 변경 전 계약 실패 확인**

Run:

```powershell
$r = Get-Content README.md -Raw
if ($r -notmatch 'h8MerbgmRRY' -and
    $r -notmatch 'csv-cleaner-sample-report.html' -and
    $r -match '31 automated tests') { 'EXPECTED FAIL' } else { exit 1 }
```

Expected: `EXPECTED FAIL`

- [x] **Step 2: README 최소 수정**

상단 CTA 아래에 실제 영상·샘플 보고서 링크와 고정 표본 범위를 추가하고,
검증 절의 `31 automated tests`를 `32 automated tests`로 바꾼다.

- [x] **Step 3: 정적 계약 검사**

Run:

```powershell
$r = Get-Content README.md -Raw
@(
  ([regex]::Matches($r, 'h8MerbgmRRY')).Count -eq 1
  ([regex]::Matches($r, 'csv-cleaner-sample-report.html')).Count -eq 1
  $r -match '32 automated tests'
  $r -notmatch '31 automated tests'
  $r -match '11,174,017 bytes'
  $r -match '454E5027D3423A792E47B7297AC07C5371D7AAE4486008F3A964A71BEB1D39B1'
) -notcontains $false
```

Expected: `True`

- [x] **Step 4: 링크 응답 검사**

Run:

```powershell
$urls = @(
  'https://github.com/loved0543-dotcom/csv-audit-cleaner-lite/releases/download/v1.0.0/CSV_Audit_Cleaner_Lite_v1.0.zip',
  'https://lovelife717.gumroad.com/l/csv-audit-cleaner',
  'https://oneeyeview-automation.vercel.app',
  'https://www.youtube.com/watch?v=h8MerbgmRRY',
  'https://oneeyeview-automation.vercel.app/csv-cleaner-sample-report.html'
)
foreach ($url in $urls) {
  (Invoke-WebRequest $url -MaximumRedirection 5 -UseBasicParsing).StatusCode
}
```

Expected: 다섯 응답 모두 `200`

- [x] **Step 5: 커밋·푸시·공개 검증**

Run:

```powershell
git add README.md docs/superpowers
git commit -m "docs: link CSV cleaner proof from Lite README"
git push origin HEAD
```

Expected: push 성공. 공개 GitHub README에서 영상·보고서·32개 검사가 보이고,
낡은 31개 표기는 없다.

## 실행 결과

- 공개 커밋: `fcc9c11b68d5910793f0d77661f25e56fbc77c3a`
- 공개 GitHub HTML·raw README HTTP `200`
- 영상 ID·샘플 보고서 URL 각 1회, `32 automated tests` 확인
- 낡은 `31 automated tests` 없음
- 기존 Lite ZIP URL·크기·SHA-256 유지
- 대상 외부 링크 5개 모두 HTTP `200`
