def solution(X, Y, D):
    steps = ((Y - X) // D)
    if (Y - X) % D == 0:
        return steps
    steps += 1
    return steps
