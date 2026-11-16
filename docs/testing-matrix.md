# 🧪 Browser and page test matrix

## Purpose

This matrix makes manual testing repeatable. It is a template for recording real results, not a statement that every browser has already passed.

## Page coverage

| Test | Home | About | Media |
|---|---:|---:|---:|
| Direct URL loads | Required | Required | Required |
| Navigation links | Required | Required | Required |
| Local CSS and images | Required | Required | Required |
| Console errors reviewed | Required | Required | Required |
| Mobile viewport | Required | Required | Required |
| Desktop viewport | Required | Required | Required |
| Keyboard-only navigation | Required | Required | Required |
| 200% zoom | Required | Required | Required |
| External resource failures | Required | Required | Required |
| Footer layout | Required | Required | Required |

## Browser coverage

| Browser | Platform | Required viewport coverage | Result |
|---|---|---|---|
| Chrome or Chromium | Windows/macOS/Linux | Desktop and mobile emulation | Not recorded |
| Firefox | Desktop | Desktop | Not recorded |
| Safari | macOS/iOS | Desktop and mobile | Not recorded |
| Edge | Windows | Desktop | Not recorded |

## Test record template

| Field | Value |
|---|---|
| Commit SHA | Fill in |
| Date | Fill in |
| Browser/version | Fill in |
| Operating system | Fill in |
| Viewport | Fill in |
| Page | Fill in |
| Result | Pass / Fail / Not tested |
| Evidence | Screenshot or sanitized diagnostic |
| Follow-up issue | Link if applicable |

## Exit criteria

Do not mark a release browser-tested until every required page has been opened directly, local assets have been checked, the main interactive carousel has been exercised, and responsive and keyboard checks have been completed.
