from src.recommendation.data_structures import UserProfile
from src.recommendation.engine import CollaborativeFilter


def test_recommendations_basic():
    users = {
        1: UserProfile(user_id=1, purchases={1, 2, 3}, ratings={1: 5, 2: 4, 3: 3}),
        2: UserProfile(user_id=2, purchases={2, 3, 4}, ratings={2: 4, 3: 4, 4: 4}),
        3: UserProfile(user_id=3, purchases={3, 5, 6}, ratings={3: 3, 5: 3, 6: 5}),
    }
    cf = CollaborativeFilter(users)
    recs = cf.recommend(target_user_id=1, k=2)

    rec_books = {r.book_id for r in recs}
    assert 4 in rec_books or 6 in rec_books
