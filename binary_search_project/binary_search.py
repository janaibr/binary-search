# binary_search.py
from dataclasses import dataclass
from typing import List

@dataclass
class SearchResult:
    index: int
    comparisons: int

def binary_search(arr: List[int], target: int) -> SearchResult:
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            return SearchResult(mid, comparisons)
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return SearchResult(-1, comparisons)