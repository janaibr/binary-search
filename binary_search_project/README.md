# Binary Search Performance Analysis

This mini‑project benchmarks **Binary Search** against a **Linear Search** baseline across multiple input sizes and scenarios.

## What you get
- `binary_search.py`, `linear_search.py`: instrumented implementations
- `experiment.py`: reproducible experiment harness
- `results.csv`: aggregated median/mean timings and comparisons
- Charts in `./charts/` showing time and comparisons vs. N
- A short report in `REPORT.md`

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python experiment.py
```

## Scenarios
- `present_low`: target at index 0
- `present_mid`: target at middle
- `present_high`: target at last index
- `absent`: target is missing

## Notes
- Binary Search performs in **O(log N)** comparisons, while Linear Search performs in **O(N)** in the worst case.
- Actual timings vary due to CPU and OS; comparisons are hardware‑independent and track algorithmic complexity.