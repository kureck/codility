def solution(A):
    east = 0
    passing = 0

    for i in A:
        if i == 1:
            passing += east
            if passing > 1000000000:
                return -1
        else:
            east += 1

    return passing
