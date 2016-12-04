def solution(X, A):
    aux_array = [0] * (len(A) + 1)

    for i in range(len(A)):
        try:
            if aux_array[A[i]] == 0:
                aux_array[A[i]] = A[i]
                X -= 1
            if X == 0:
                return i
        except:
            return -1
    return -1
