# Binary Search Performance Analysis — Report

**Goal.** Empirically validate the theoretical efficiency of Binary Search compared to Linear Search on sorted arrays of increasing size, and quantify both **runtime** and **number of comparisons** under different target scenarios.

## Methods
- **Data.** Deterministic arrays `0..N-1` with N in {200..500,000}.
- **Algorithms.** Instrumented Binary Search and Linear Search.
- **Scenarios.** Target at beginning (`present_low`), middle (`present_mid`), end (`present_high`), and missing (`absent`).
- **Metric.** Median nanoseconds over 5 runs per (N, scenario, algorithm) and median comparisons.

## Key Findings
- **Comparisons grow logarithmically** for Binary Search and **linearly** for Linear Search.
- For **present_low**, Linear Search is relatively advantaged (best‑case), but Binary Search still scales better for larger N.
- For **absent** or **present_high**, Linear Search approaches **N** comparisons, while Binary Search stays near **⌈log2 N⌉**.
- Runtime charts mirror comparison trends despite system noise.

## Evidence (Charts)
See `charts/`:
- `time_vs_n_*.png`: median runtime vs. N for each scenario.
- `comparisons_vs_n_*.png`: median comparisons vs. N for each scenario.

## Conclusion
Binary Search demonstrates **O(log N)** behavior in practice, dominating Linear Search for large N across typical scenarios—especially when the element is near the end or absent. The number of comparisons offers a robust, hardware‑independent view confirming theory.

## Reproducibility
- Python 3.9+
- `requirements.txt` included
- Run `python experiment.py` to regenerate `results.csv` (and recreate charts if you add plotting).