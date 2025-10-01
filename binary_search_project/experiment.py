# experiment.py
import time, math, random
from dataclasses import dataclass
from typing import List, Tuple, Callable
import pandas as pd

from binary_search import binary_search, SearchResult as BSResult
from linear_search import linear_search, SearchResult as LSResult

@dataclass
class TrialConfig:
    n: int
    scenario: str  # 'present_low','present_mid','present_high','absent' or 'all'
    trials: int

def run_trial(algorithm: Callable[[List[int], int], BSResult], arr: List[int], target: int):
    start = time.perf_counter_ns()
    result = algorithm(arr, target)
    end = time.perf_counter_ns()
    return (end - start), result.comparisons

def prepare_targets(arr: List[int], scenario: str) -> int:
    n = len(arr)
    if scenario == 'present_low':
        return arr[0]
    if scenario == 'present_mid':
        return arr[n // 2]
    if scenario == 'present_high':
        return arr[-1]
    if scenario == 'absent':
        return arr[-1] + 1
    raise ValueError("Unknown scenario")

def run_experiments(configs: List[TrialConfig]):
    rows = []
    for cfg in configs:
        arr = list(range(cfg.n))
        scenarios = [cfg.scenario] if cfg.scenario != "all" else ['present_low','present_mid','present_high','absent']
        for scenario in scenarios:
            target = prepare_targets(arr, scenario)
            for _ in range(cfg.trials):
                t_bin, c_bin = run_trial(binary_search, arr, target)
                t_lin, c_lin = run_trial(linear_search, arr, target)
                rows.append({"n": cfg.n, "scenario": scenario, "algorithm": "binary_search", "time_ns": t_bin, "comparisons": c_bin})
                rows.append({"n": cfg.n, "scenario": scenario, "algorithm": "linear_search", "time_ns": t_lin, "comparisons": c_lin})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    sizes = [200, 500, 1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000]
    configs = [TrialConfig(n=n, scenario="all", trials=5) for n in sizes]
    df = run_experiments(configs)
    agg = (df.groupby(["n","scenario","algorithm"], as_index=False)
             .agg(time_ns_median=("time_ns","median"),
                  time_ns_mean=("time_ns","mean"),
                  comparisons_median=("comparisons","median"),
                  comparisons_mean=("comparisons","mean")))
    agg.to_csv("results.csv", index=False)
    print("Saved results.csv")