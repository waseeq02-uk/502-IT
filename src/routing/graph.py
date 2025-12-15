from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import numpy as np


@dataclass(frozen=True)
class Point:
    """2D point for Euclidean TSP."""
    x: float
    y: float


class Graph:
    """
    Complete weighted graph for Euclidean TSP.
    Stores points and a precomputed distance matrix.
    """

    def __init__(self, points: List[Point]):
        if not points:
            raise ValueError("Graph requires at least 1 point.")
        self.points: List[Point] = points
        self.n: int = len(points)
        self.dist: np.ndarray = self._compute_dist_matrix(points)

    @staticmethod
    def _compute_dist_matrix(points: List[Point]) -> np.ndarray:
        n = len(points)
        dist = np.zeros((n, n), dtype=float)
        for i in range(n):
            for j in range(i + 1, n):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                d = float((dx * dx + dy * dy) ** 0.5)
                dist[i, j] = d
                dist[j, i] = d
        return dist

    def distance(self, i: int, j: int) -> float:
        return float(self.dist[i, j])

    def size(self) -> int:
        return self.n

    def as_numpy(self) -> np.ndarray:
        return self.dist.copy()

    def coords(self) -> List[Tuple[float, float]]:
        return [(p.x, p.y) for p in self.points]
