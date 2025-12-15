from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Set


@dataclass
class UserProfile:
    user_id: int
    purchases: Set[int]                  # set of book ids
    ratings: Dict[int, float]            # book_id -> rating (1..5)
