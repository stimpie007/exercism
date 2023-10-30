import itertools


def combinations(target, size, exclude):
    candidates = [i for i in range(1, min(target, 9) + 1) if i not in exclude]
    return [list(combo) for combo in itertools.combinations(candidates, size) if sum(combo) == target]
