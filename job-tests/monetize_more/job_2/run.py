def solution(A):
    sorted_list = sorted(A)

    for i in range(len(A)):
        for j in range(1, len(A) + 1):
            if A[i] < A[-j] or A[i] == A[-j]:
                continue
            else:
                A[i], A[-j] = A[-j], A[i]
                if A == sorted_list:
                    return True
                else:
                    return False

    return False
