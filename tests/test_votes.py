import pytest
from first_task.votes import vote


@pytest.mark.parametrize(
    "votes, expected",
    [
        ([1, 1, 1, 2, 3], 1),
        ([1, 2, 3, 2, 2], 2),
        ([3, 2, 3, 3, 2], 2),
    ],
)
def test_vote(votes, expected):
    assert vote(votes) == expected
