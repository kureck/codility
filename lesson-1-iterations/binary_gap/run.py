def solution(N):
    cnt = 0
    result = 0
    one = False

    while N:
        if N & 1 == 1:
            if (one == True):
                result = max(result,cnt)
            else:
                one = True
            cnt = 0
        else:
            cnt += 1
        N >>= 1

    return result
