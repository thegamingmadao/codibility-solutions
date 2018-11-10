def solution(N, A):
    n_list = [0 for n in range(N)]
    i = 0
    while i < len(A):
        if A[i] == N + 1:
            n_list = [max(n_list) for n in n_list]
        else:
            n_list[A[i] -1] += 1
        i += 1
    return n_list