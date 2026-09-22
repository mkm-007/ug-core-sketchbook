# UG Core Sketchbook

2026 portfolio rebuilds of **high-signal UG cores** (GITAM ECE AIML). One mini-project per course — not full lab dumps.

**Honesty:** Current dates only. Not backdated UG submissions.

| Module | Course root | Demo |
|--------|-------------|------|
| `dsa` | DSA with Python | tested sorting + search kit |
| `ml_classic` | Machine Learning | logistic regression on synthetic blobs |
| `dl_mini` | Deep Learning | tiny MLP from scratch (numpy) |
| `networks` | Communication Networks | stop-and-wait ARQ sim |
| `dbms` | Intro to DBMS | SQLite schema + queries |
| `mpmc_iot` | MPMC / IoT | register-level GPIO bit bang sim |

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```
