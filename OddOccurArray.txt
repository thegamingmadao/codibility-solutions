def solution(A):
    # write your code in Python 3.6
    n = 0
    A.sort()
    while len(A) > 1:
        if A[n] == A[n+1]:
            del A[:2]
        else:
            break
    return A[n]