def solution(A):
    if len(A) == 0:
        return len(A)
    if A[0] == 0:
        return 1
    l = []
    l.append(A[0])
    for i in range(1, len(A)):
        if A[i - 1] == -1:
            l.append(A[i])
            return len(l)
        l.append(A[A[i - 1]])

    return len(l)
