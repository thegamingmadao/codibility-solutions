def solution(A):
    # write your code in Python 3.6
    return min(abs(sum(A[:i])-sum(A[i:])) for i in range(1,len(A)))