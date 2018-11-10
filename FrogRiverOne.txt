def solution(X, A):
    # write your code in Python 3.6
    x=1
    tmp_list=[]
    while x in A:
        tmp_list.append(A.index(x))
        if x == X:
            return max(tmp_list)
        else:
            x +=1
    return -1