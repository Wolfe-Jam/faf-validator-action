# WJTTC Test Suite: faf-validator-action

**Project:** FAF DNA Validator GitHub Action
**Version:** 1.0.0
**Date:** 2026-01-29
**Tester:** WJTTC Automated Suite
**Philosophy:** "We break things so others never have to know they were broken."

---

## Test Summary

| Tier | Category | Tests | Target Pass Rate |
|------|----------|-------|------------------|
| T1 | Brake (Critical) | 6 | 100% |
| T2 | Engine (Core) | 10 | 100% |
| T3 | Aero (Polish) | 8 | 95% |
| **Total** | | **24** | **98%** |

---

## Tier 1: BRAKE SYSTEMS 🚨 (Critical)

**When failure = build breaks incorrectly or passes when it shouldn't**

### T1.1 - Missing project.faf
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Run with no project.faf | Exit code 1 | | |
| Error message contains "not found" | Yes | | |
| No GEMINI.md modification | Unchanged | | |

### T1.2 - Invalid YAML
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Malformed YAML (unclosed bracket) | Exit code 1 | | |
| Error message contains "Invalid YAML" | Yes | | |
| Duplicate keys in YAML | Exit or warn | | |

### T1.3 - Score Below Minimum (Build Gate)
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Score 50%, min 85% | Exit code 1 | | |
| Score 84%, min 85% | Exit code 1 | | |
| Score 85%, min 85% | Exit code 0 | | |
| Error shows required vs current | Yes | | |

### T1.4 - Exit Codes
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Success → exit 0 | Exit code 0 | | |
| Missing file → exit 1 | Exit code 1 | | |
| Invalid YAML → exit 1 | Exit code 1 | | |
| Below minimum → exit 1 | Exit code 1 | | |

### T1.5 - No Data Loss
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| GEMINI.md body preserved after sync | Identical | | |
| project.faf never modified | Unchanged | | |
| Frontmatter only updated | Yes | | |

### T1.6 - Empty/Null File Handling
**Status:** ⏳ PENDING
**Priority:** CRITICAL

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Empty project.faf (0 bytes) | Exit code 1 | | |
| project.faf with only whitespace | Exit code 1 or score 0 | | |
| Null values in required fields | Handled gracefully | | |

---

## Tier 2: ENGINE SYSTEMS ⚡ (Core Functionality)

**When failure = incorrect scores or broken sync**

### T2.1 - Score Calculation Accuracy
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| 0/21 slots filled | 0% | | |
| 21/21 slots filled | 100% | | |
| 10/21 slots filled | 47% | | |
| 18/21 slots filled | 85% | | |
| 21/21 slots + extra fields | 100% (ignore extra) | | |

### T2.2 - Tier Assignment
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Score 100% | Trophy | | |
| Score 99% | Gold | | |
| Score 95% | Silver | | |
| Score 85% | Bronze | | |
| Score 70% | Green | | |
| Score 55% | Yellow | | |
| Score 54% | Red | | |
| Score 0% | Red | | |

### T2.3 - GEMINI.md Bi-Sync
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| faf_score in frontmatter | Updated | | |
| faf_tier in frontmatter | Updated | | |
| last_sync timestamp | Updated | | |
| Body content preserved | Identical | | |

### T2.4 - CLI Argument Parsing
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| --min-score 50 | Uses 50 | | |
| --min-score 100 | Uses 100 | | |
| No argument | Uses default 85 | | |
| --help | Shows usage | | |
| Invalid argument | Error message | | |

### T2.5 - Minimum Score Boundaries
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| --min-score 0 | Always passes | | |
| --min-score 100 | Only 100% passes | | |
| --min-score 101 | Error or never passes | | |
| --min-score -1 | Error or always passes | | |

### T2.6 - TBD Value Handling
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Field with "TBD" | Not counted as filled | | |
| Field with "tbd" (lowercase) | Check handling | | |
| Field with "" (empty string) | Not counted as filled | | |
| Field with null | Not counted as filled | | |

### T2.7 - Generated Timestamp
**Status:** ⏳ PENDING
**Priority:** MEDIUM

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| generated field present | Used for last_sync | | |
| generated field missing | "unknown" fallback | | |
| generated field malformed | Handled gracefully | | |

### T2.8 - Multiple Runs Idempotency
**Status:** ⏳ PENDING
**Priority:** MEDIUM

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Run twice, same input | Same output | | |
| Run twice, no file changes | GEMINI.md unchanged | | |

### T2.9 - File Encoding
**Status:** ⏳ PENDING
**Priority:** MEDIUM

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| UTF-8 with BOM | Handles correctly | | |
| UTF-8 without BOM | Handles correctly | | |
| ASCII only | Handles correctly | | |

### T2.10 - action.yml Validity
**Status:** ⏳ PENDING
**Priority:** HIGH

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Valid composite action | Yes | | |
| Python version specified | 3.12 | | |
| Default min_score | 85 | | |
| Branding icon | check-circle | | |
| Branding color | orange | | |

---

## Tier 3: AERODYNAMICS 🏁 (Polish)

**When failure = minor UX issues**

### T3.1 - Output Formatting
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Score includes emoji 📊 | Yes | | |
| Success includes ✅ | Yes | | |
| Failure includes ❌ | Yes | | |
| Info includes ℹ️ | Yes | | |

### T3.2 - Score Boundary Edge Cases
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Exactly 85% (boundary) | Bronze, passes at min 85 | | |
| Exactly 84.9% (rounds to?) | Check rounding | | |
| Exactly 100% | Trophy | | |

### T3.3 - Missing GEMINI.md (Graceful)
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| No GEMINI.md file | Skips sync, no error | | |
| Logs info message | Yes | | |
| Still validates .faf | Yes | | |

### T3.4 - Special Characters in YAML
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Emoji in field values 🏎️ | Handled | | |
| Quotes in strings | Handled | | |
| Colons in values | Handled | | |
| Multiline strings | Handled | | |

### T3.5 - Unicode Content
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Japanese characters | Handled | | |
| Arabic (RTL) | Handled | | |
| Combining characters | Handled | | |

### T3.6 - Large File Handling
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| 100KB project.faf | Processes normally | | |
| 1MB project.faf | Processes or warns | | |
| 100+ extra fields | Ignores, no crash | | |

### T3.7 - Console Output Formatting
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Percentage has % symbol | Yes | | |
| Tier name in parentheses | Yes | | |
| Required vs Current aligned | Yes | | |

### T3.8 - Dependency Availability
**Status:** ⏳ PENDING
**Priority:** LOW

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| PyYAML installable | Yes | | |
| python-frontmatter installable | Yes | | |
| Python 3.12 compatible | Yes | | |

---

## Edge Cases & Stress Tests

### WJTTC Expert Layer

| Category | Test | Expected |
|----------|------|----------|
| **Injection** | YAML with `!!python/object` | Rejected (safe_load) |
| **Injection** | project.faf named `; rm -rf /` | No execution |
| **Boundary** | min_score = MAX_INT | Error or handled |
| **Boundary** | 0 slots in .faf | 0% score |
| **Race** | Two validators same file | No corruption |
| **Encoding** | Binary file as .faf | Error gracefully |

---

## Performance Targets

| Metric | Target | Measured |
|--------|--------|----------|
| Parse time (small .faf) | < 100ms | |
| Parse time (large .faf) | < 500ms | |
| Full sync cycle | < 1s | |
| Memory usage | < 50MB | |

---

## Execution Log

```
[ ] Clone repo
[ ] Create test fixtures
[ ] Run T1 tests (Critical)
[ ] Run T2 tests (Core)
[ ] Run T3 tests (Polish)
[ ] Calculate pass rate
[ ] Generate .taf receipt
```

---

## Championship Certification

| Pass Rate | Tier | Status |
|-----------|------|--------|
| 95-100% | 🏆 Championship | |
| 85-94% | 🥇 Podium | |
| 70-84% | 🥈 Points | |
| 55-69% | 🥉 Midfield | |
| <55% | 🔴 DNF | |

---

*Generated by WJTTC Builder*
*Championship Testing Standards 🏎️*
