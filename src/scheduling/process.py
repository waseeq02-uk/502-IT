from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    base_priority: int  # smaller number = higher priority

    remaining: int = field(init=False)
    start_time: int | None = None
    completion_time: int | None = None
    last_enqueued: int = 0  # for aging bookkeeping

    def __post_init__(self) -> None:
        if self.arrival < 0:
            raise ValueError("arrival must be >= 0")
        if self.burst <= 0:
            raise ValueError("burst must be > 0")
        if self.base_priority <= 0:
            raise ValueError("priority must be >= 1")
        self.remaining = self.burst

    def is_complete(self) -> bool:
        return self.remaining <= 0
