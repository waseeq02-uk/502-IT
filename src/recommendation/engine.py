from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Dict, List, Set, Tuple
import heapq

from .data_structures import UserProfile
from .similarity import jaccard


@dataclass
class Recommendation:
    book_id: int
    score: float


class CollaborativeFilter:
    """
    User-user collaborative filtering using:
      - inverted index (book -> users)
      - Jaccard similarity on purchase sets
      - weighted rating aggregation
    """

    def __init__(self, users: Dict[int, UserProfile]):
        if not users:
            raise ValueError("users must not be empty")
        self.users = users
        self.inverted_index: Dict[int, Set[int]] = self._build_inverted_index()

    def _build_inverted_index(self) -> Dict[int, Set[int]]:
        index: DefaultDict[int, Set[int]] = defaultdict(set)
        for uid, profile in self.users.items():
            for book in profile.purchases:
                index[book].add(uid)
        return dict(index)

    def recommend(self, target_user_id: int, k: int = 5, top_sim_users: int = 50) -> List[Recommendation]:
        if k <= 0:
            return []
        if target_user_id not in self.users:
            raise KeyError("target_user_id not found")

        target = self.users[target_user_id]
        target_books = target.purchases

        # Candidate users via inverted index
        intersections: DefaultDict[int, int] = defaultdict(int)
        for b in target_books:
            for uid in self.inverted_index.get(b, set()):
                if uid != target_user_id:
                    intersections[uid] += 1

        # Compute similarity only for candidates
        sims: List[Tuple[float, int]] = []
        for uid in intersections:
            sim = jaccard(target_books, self.users[uid].purchases)
            if sim > 0.0:
                sims.append((sim, uid))

        sims.sort(reverse=True)  # highest similarity first
        sims = sims[:top_sim_users]

        # Aggregate candidate book scores
        scores: DefaultDict[int, float] = defaultdict(float)
        for sim, uid in sims:
            prof = self.users[uid]
            for book in prof.purchases:
                if book in target_books:
                    continue
                rating = prof.ratings.get(book, 0.0)
                scores[book] += sim * rating

        # Top-k extraction
        heap: List[Tuple[float, int]] = []
        for book, score in scores.items():
            if len(heap) < k:
                heapq.heappush(heap, (score, book))
            else:
                if score > heap[0][0]:
                    heapq.heapreplace(heap, (score, book))

        heap.sort(reverse=True)
        return [Recommendation(book_id=book, score=score) for score, book in heap]
