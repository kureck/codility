# 66%
def solution(N, A):
    result = [0] * N

    for i in A:
        if 1 <= i <= N:
            result[i - 1] += 1
        if i > N:
            max_num = max(result)
            result = [max_num] * N

    return result

# 77%
def solution2(N, A):
    result = [0] * N
    max_count = 0

    for i in A:
        if 1 <= i <= N:
            result[i - 1] += 1
            max_count = max(result[i - 1], max_count)
        if i > N:
            result = [max_count] * N

    return result
