from __future__ import annotations

import random
from pathlib import Path

from src.routing.graph import Graph, Point
from src.routing.tsp_solver import TSPSolver

from src.scheduling.process import Process
from src.scheduling.scheduler import PriorityAgingScheduler

from src.recommendation.engine import CollaborativeFilter
from src.recommendation.data_structures import UserProfile

from src.utils.visualisation import plot_complete_graph, plot_tour


def run_tsp_demo(out_dir: Path) -> None:
    print("\n=== TSP Demo (Nearest Neighbour + 2-opt) ===")

    random.seed(42)
    points = [Point(random.random() * 100, random.random() * 100) for _ in range(15)]
    g = Graph(points)

    solver = TSPSolver(start=0, apply_two_opt=True)
    sol = solver.solve(g)

    print(f"Tour: {sol.tour}")
    print(f"Length: {sol.length:.2f}")

    coords = g.coords()
    plot_complete_graph(coords, str(out_dir / "tsp_complete_graph.png"))
    plot_tour(coords, sol.tour, str(out_dir / "tsp_tour.png"))
    print(f"Saved figures to: {out_dir}")


def run_scheduler_demo() -> None:
    print("\n=== Scheduler Demo (Preemptive Priority + Aging) ===")

    procs = [
        Process(pid="P1", arrival=0, burst=5, base_priority=3),
        Process(pid="P2", arrival=1, burst=3, base_priority=1),
        Process(pid="P3", arrival=2, burst=2, base_priority=2),
        Process(pid="P4", arrival=3, burst=4, base_priority=4),
    ]
    sched = PriorityAgingScheduler(aging_interval=10)
    result = sched.run(procs)

    print("Timeline (per tick):")
    print(" ".join(result.timeline))
    print("Completion times:", result.completion_times)
    print("Waiting times:", result.waiting_times)
    print(f"Average waiting time: {result.average_waiting_time:.2f}")


def build_small_reco_dataset() -> dict[int, UserProfile]:
    """
    A small dataset that guarantees recommendations exist.
    Books are integers, ratings are 1..5.
    """
    return {
        1: UserProfile(user_id=1, purchases={101, 102, 103}, ratings={101: 5, 102: 4, 103: 3}),
        2: UserProfile(user_id=2, purchases={102, 103, 104, 105}, ratings={102: 4, 103: 5, 104: 4, 105: 3}),
        3: UserProfile(user_id=3, purchases={103, 106, 107}, ratings={103: 4, 106: 3, 107: 5}),
        4: UserProfile(user_id=4, purchases={101, 108, 109}, ratings={101: 4, 108: 5, 109: 4}),
    }


def run_recommendation_demo() -> None:
    print("\n=== Recommendation Demo (User-User CF + Jaccard + Inverted Index) ===")

    users = build_small_reco_dataset()
    engine = CollaborativeFilter(users)

    target_user = 1
    recs = engine.recommend(target_user_id=target_user, k=5)

    print(f"Target user: U{target_user}")
    print(f"Purchases: {sorted(users[target_user].purchases)}")
    print("Top recommendations:")
    for r in recs:
        print(f"  Book {r.book_id}  | score={r.score:.3f}")


def main() -> None:
    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)

    run_tsp_demo(out_dir)
    run_scheduler_demo()
    run_recommendation_demo()


if __name__ == "__main__":
    main()
