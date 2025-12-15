from __future__ import annotations

from typing import List
import numpy as np


def tour_length(tour: List[int], dist: np.ndarray) -> float:
    """Compute total length of a closed tour."""
    if len(tour) < 2:
        return 0.0
    total = 0.0
    for i in range(1, len(tour)):
        total += float(dist[tour[i - 1], tour[i]])
    return total


def two_opt_improve(tour: List[int], dist: np.ndarray, eps: float = 1e-12) -> List[int]:
    """
    2-opt local search until no improving move exists.

    Complexity:
      - One full pass: O(n^2)
      - Multiple passes until convergence: typically small; worst-case higher.
    """
    if len(tour) < 4:
        return tour

    n = len(tour)
    improved = True

    while improved:
        improved = False

        # i and j define the segment [i:j) to reverse
        for i in range(1, n - 2):
            for j in range(i + 2, n - 1):
                a, b = tour[i - 1], tour[i]
                c, d = tour[j], tour[j + 1]

                # current edges: (a,b) + (c,d)
                # proposed edges: (a,c) + (b,d)
                delta = (dist[a, b] + dist[c, d]) - (dist[a, c] + dist[b, d])

                if delta > eps:  # strict improvement
                    tour[i : j + 1] = reversed(tour[i : j + 1])
                    improved = True
                    break
            if improved:
                break

    return tour
