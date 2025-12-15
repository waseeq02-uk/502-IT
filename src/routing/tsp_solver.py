from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
import numpy as np

from .graph import Graph
from .optimisers import two_opt_improve, tour_length


@dataclass
class TSPSolution:
    tour: List[int]          # closed tour, ends where it started
    length: float            # total distance


class TSPSolver:
    """
    Enhanced Nearest Neighbour + 2-opt for Euclidean metric TSP.
    """

    def __init__(self, start: int = 0, apply_two_opt: bool = True):
        self.start = start
        self.apply_two_opt = apply_two_opt

    def solve(self, graph: Graph) -> TSPSolution:
        n = graph.size()
        if self.start < 0 or self.start >= n:
            raise ValueError("Invalid start index.")

        dist = graph.as_numpy()
        tour = self._nearest_neighbour(dist, start=self.start)

        if self.apply_two_opt:
            tour = two_opt_improve(tour, dist)

        length = tour_length(tour, dist)
        return TSPSolution(tour=tour, length=length)

    @staticmethod
    def _nearest_neighbour(dist: np.ndarray, start: int = 0) -> List[int]:
        n = dist.shape[0]
        unvisited = set(range(n))
        unvisited.remove(start)

        tour = [start]
        current = start

        while unvisited:
            # deterministic tie-break by index (min index among min distance)
            next_city: Optional[int] = None
            best_d = float("inf")
            for u in unvisited:
                d = float(dist[current, u])
                if d < best_d or (abs(d - best_d) < 1e-15 and (next_city is None or u < next_city)):
                    best_d = d
                    next_city = u

            assert next_city is not None
            tour.append(next_city)
            unvisited.remove(next_city)
            current = next_city

        tour.append(start)  # close tour
        return tour
