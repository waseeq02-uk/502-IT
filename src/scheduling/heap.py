from __future__ import annotations

import heapq
from typing import Any, Dict, List, Tuple

_REMOVED = object()


class BinaryHeap:
    """
    Priority queue with lazy deletion.
    Supports insert/update and extract_min.
    """
    def __init__(self) -> None:
        self._heap: List[list] = []
        self._entry_finder: Dict[Any, list] = {}
        self._counter: int = 0

    def __len__(self) -> int:
        return len(self._entry_finder)

    def is_empty(self) -> bool:
        return len(self._entry_finder) == 0

    def insert(self, item: Any, priority: Tuple[int, int, int]) -> None:
        """
        priority tuple example: (effective_priority, arrival_time, tie_counter)
        """
        if item in self._entry_finder:
            self.remove(item)
        entry = [priority, self._counter, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._heap, entry)
        self._counter += 1

    def remove(self, item: Any) -> None:
        entry = self._entry_finder.pop(item)
        entry[2] = _REMOVED

    def extract_min(self) -> Any:
        while self._heap:
            priority, count, item = heapq.heappop(self._heap)
            if item is not _REMOVED:
                del self._entry_finder[item]
                return item
        raise KeyError("Empty heap")

    def peek_min_priority(self) -> Tuple[int, int, int]:
        while self._heap:
            priority, count, item = self._heap[0]
            if item is _REMOVED:
                heapq.heappop(self._heap)
                continue
            return priority
        raise KeyError("Empty heap")
