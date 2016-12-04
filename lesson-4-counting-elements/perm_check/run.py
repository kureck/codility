def solution(A):
    aux_array = [0] * (len(A) + 1)
    for i in A:
        try:
            aux_array[i] = i
        except:
            return 0
    aux_array.pop(0)

    return 1 if 0 not in aux_array else 0
