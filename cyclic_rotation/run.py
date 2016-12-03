def solution(A, K):
    if not A:
        return A
    if K > len(A):
        K = K % len(A)
    shift = len(A) - K
    return A[shift:] + A[:shift]
