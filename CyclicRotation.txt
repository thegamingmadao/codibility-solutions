def solution(A, K):
    # write your code in Python 3.6
    if A:
        for i in range (0,K):
            A.insert(0, A.pop(-1))#Remove last element of A and insert into index 0 of A shifting the rest right
    return A