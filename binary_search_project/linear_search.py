# linear_search.py
from dataclasses import dataclass
from typing import List

@dataclass
class SearchResult:
    index: int
    comparisons: int

def linear_search(arr: List[int], target: int) -> SearchResult:
    comparisons = 0
    for i, v in enumerate(arr):
        comparisons += 1
        if v == target:
            return SearchResult(i, comparisons)
    return SearchResult(-1, comparisons)