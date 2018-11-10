def solution(A):
    # write your code in Python 3.6
    a = set(A)
    if len(a) == len(A) and sum(a) == sum(range(1,len(a)+1)):
        return 1
    else:
        return 0
