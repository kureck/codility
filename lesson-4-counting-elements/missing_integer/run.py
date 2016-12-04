def solution(A):
    aux_array = [0] * (len(A) + 1)
    size = len(A)

    for i in A:
        if 1 <= i <= size + 1:
            aux_array[i - 1] = 1

    for i in range(len(aux_array) + 1):
        if aux_array[i] == 0:
            return i + 1

    return -1


def solution2(A):
    positives = set((value for value in A if value > 0))
    return next((i for i in range(1, len(A) + 2) if i not in positives), 1)
