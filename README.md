# iomarkets-repro-test

A tiny fixture for testing [iomarkets.dev](https://iomarkets.dev): the Issue Sweeper's bug reproduction, races with a locked reproduction test, and the line's pull request checks. `textkit.py` has a known bug, reported in an issue.

## Development

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e '.[test]'
pytest
```
