def solution(A):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if j-i <= A[i] + A[j]:
                count += 1
    return count