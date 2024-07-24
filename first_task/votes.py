def vote(votes):
    max_ = 0
    set_votes = set(votes)
    for vote in set_votes:
        if votes.count(vote) > max_:
            max_ = vote
    return max_


if __name__ == '__main__':
    """
    1
    2
    """
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))