def solution(A):
    # write your code in Python 3.6
    sum= 0
    n = len(A)
    p = [0] * (n + 1)
    for k in range(1, n+1):
        p[k] = p[k-1] + A[k-1]
    for k in range(n):
        if A[k] == 0:
            sum += p[n] - p[k]
    if sum > 1000000000:
        return -1
    else:
        return sum