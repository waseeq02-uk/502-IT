from src.routing.graph import Graph, Point
from src.routing.tsp_solver import TSPSolver


def test_tsp_returns_closed_tour():
    points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
    g = Graph(points)
    solver = TSPSolver(start=0, apply_two_opt=True)
    sol = solver.solve(g)

    assert sol.tour[0] == sol.tour[-1]
    assert len(sol.tour) == g.size() + 1
    assert sol.length > 0
