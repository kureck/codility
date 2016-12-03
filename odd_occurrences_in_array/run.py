def solution(A):
    if len(A) == 0:
        return None
    hash_count = {}
    for i in A:
        if hash_count.get(i) is None:
            hash_count[i] = 0
        hash_count[i] += 1
    for k, v in hash_count.items():
        if v % 2 != 0:
            return k
