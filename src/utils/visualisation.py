from __future__ import annotations

from typing import List, Tuple
import matplotlib.pyplot as plt
import networkx as nx


def plot_complete_graph(coords: List[Tuple[float, float]], save_path: str) -> None:
    G = nx.complete_graph(len(coords))
    pos = {i: coords[i] for i in range(len(coords))}
    nx.draw(G, pos, with_labels=True)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_tour(coords: List[Tuple[float, float]], tour: List[int], save_path: str) -> None:
    xs = [coords[i][0] for i in tour]
    ys = [coords[i][1] for i in tour]
    plt.plot(xs, ys, marker="o")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
