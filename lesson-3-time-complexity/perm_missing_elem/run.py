def solution(A):
    sum_all_should_be = sum(range(len(A) + 2))
    sum_all = sum(A)
    return sum_all_should_be - sum_all
