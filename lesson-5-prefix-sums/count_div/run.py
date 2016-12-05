# naive solution. Fails in performance... memory errors for big values
def naive_solution(A, B, K):
    count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            count += 1

    return count


def solution(A, B, K):
    floor = int(B / K)
    ceiling = -(-A // K)
    return floor - ceiling + 1
