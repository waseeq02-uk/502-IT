from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable, Any, Dict


@dataclass
class BenchmarkResult:
    seconds: float
    meta: Dict[str, Any]


def benchmark(fn: Callable[[], Any], repeats: int = 3) -> BenchmarkResult:
    if repeats <= 0:
        repeats = 1
    t0 = time.perf_counter()
    out = None
    for _ in range(repeats):
        out = fn()
    t1 = time.perf_counter()
    return BenchmarkResult(seconds=(t1 - t0) / repeats, meta={"last_result_type": type(out).__name__})
