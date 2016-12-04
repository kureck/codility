def solution(A):
    head = A[0]
    tail = sum(A[1:])
    result = abs(head - tail)

    for i in range(1, len(A) - 1):
        head += A[i]
        tail -= A[i]
        min_value = abs(head - tail)
        result = min(result, min_value)

    return result
