# QA Interactive Tool

A Python / Playwright browser-automation prototype for inspecting page links, exercising a form field, and recording navigation steps.

**Created by Valentino Herrera** · Python · Playwright · pytest · Docker · GitHub Actions

![CI](https://github.com/NOVALENTI/qa-interactive-tool/actions/workflows/main.yml/badge.svg)

## What it does
- **Link inventory**: extracts links from a page and writes structured JSON. It does not yet check every link's HTTP status.
- **Form interaction**: types a test value into a form field, but does not yet validate full form submission.
- **Journey logging**: captures navigation steps. Search-flow execution is still a prototype.
- **Testing and CI**: pytest tests plus a GitHub Actions workflow.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
python main.py --tool links --url https://example.com
```

Run interactive mode with `python main.py` or the tests with `PYTHONPATH=. pytest -q`.

## Structure
- `main.py` — CLI entry point and menu
- `src/links.py` — link collection
- `src/forms.py` — form-field interaction
- `src/journey.py` — navigation logging
- `tests/` — tests
- `.github/workflows/main.yml` — GitHub Actions workflow

## Roadmap
1. Add per-link HTTP validation.
2. Move browser tests onto deterministic local fixtures.
3. Implement verified search and full form journeys.
4. Add structured error reporting and safe input restrictions.

## Responsible use
Only test sites you own or have permission to test. This is a **demonstration/prototype**, not a production QA service. No production credentials are included.
