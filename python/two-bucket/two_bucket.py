"""
Exercism solution for "two-bucket"
"""
from typing import Tuple
from math import gcd

def measure(left: int, right: int, goal: int, fill_first: str) -> Tuple[int, str, int]:
    """
    Solve the two bucket problem given an initial state and goal, if possible.
    """
    if goal % gcd(left, right):
        raise ValueError(f"Goal {goal} must divide evenly by the GCD of {left} and {right}!")
    count = 1
    state, limits, names = {
        "one": ([0, left], (right, left), ("two", "one")),
        "two": ([0, right], (left, right), ("one", "two"))
    }[fill_first]
    while goal not in state:
        if state[0] == 0 and limits[0] == goal:
            state[0] = goal
        elif state[1] == 0 and limits[1] == goal:
            state[1] = goal
        elif state[0] == limits[0]:
            state[0] = 0
        elif state[1] == 0:
            state[1] = limits[1]
        else:
            state = [
                min(limits[0], state[0] + state[1]),
                max(0, state[1] - (limits[0] - state[0]))
            ]
        count += 1
    return count, names[state.index(goal)], state[1-state.index(goal)]