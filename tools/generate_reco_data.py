from __future__ import annotations

import json
import random
from pathlib import Path


def generate_dataset(
    n_users: int = 200,
    n_books: int = 500,
    min_books: int = 5,
    max_books: int = 30,
    seed: int = 42,
) -> dict:
    random.seed(seed)
    users = {}
    for uid in range(1, n_users + 1):
        k = random.randint(min_books, max_books)
        purchases = random.sample(range(1, n_books + 1), k=k)
        ratings = {b: random.randint(1, 5) for b in purchases}
        users[str(uid)] = {"purchases": purchases, "ratings": ratings}
    return users


def main() -> None:
    out = Path("data")
    out.mkdir(exist_ok=True)
    path = out / "users.json"

    users = generate_dataset()
    path.write_text(json.dumps(users, indent=2), encoding="utf-8")
    print(f"Wrote dataset: {path}")


if __name__ == "__main__":
    main()
