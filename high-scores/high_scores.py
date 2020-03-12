def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    list = []
    if len(scores) > 2:
        list.append(max(scores))
        for i in range(0, 2):
            scores.remove(max(scores))
            list.append(max(scores))
        return list

    if len(scores) == 2:
        list.append(max(scores))
        for i in range(0, 1):
            scores.remove(max(scores))
            list.append(max(scores))
            return list

    return scores
