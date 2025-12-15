from __future__ import annotations

import json
import argparse
from pathlib import Path

from src.recommendation.data_structures import UserProfile
from src.recommendation.engine import CollaborativeFilter


def load_users(json_path: Path) -> dict[int, UserProfile]:
    raw = json.loads(json_path.read_text(encoding="utf-8"))
    users: dict[int, UserProfile] = {}

    for uid_str, payload in raw.items():
        uid = int(uid_str)
        purchases = set(int(x) for x in payload["purchases"])
        ratings = {int(k): float(v) for k, v in payload["ratings"].items()}
        users[uid] = UserProfile(user_id=uid, purchases=purchases, ratings=ratings)

    return users


def main() -> None:
    parser = argparse.ArgumentParser(description="Run collaborative filtering recommendations.")
    parser.add_argument("--data", type=str, default="data/users.json", help="Path to users.json")
    parser.add_argument("--user", type=int, required=True, help="Target user id")
    parser.add_argument("--k", type=int, default=5, help="Top-k recommendations")
    args = parser.parse_args()

    users = load_users(Path(args.data))
    engine = CollaborativeFilter(users)

    recs = engine.recommend(target_user_id=args.user, k=args.k)

    print(f"Target user: {args.user}")
    print(f"Purchased: {sorted(users[args.user].purchases)}")
    print("Recommendations:")
    for r in recs:
        print(f"  Book {r.book_id} | score={r.score:.3f}")


if __name__ == "__main__":
    main()
