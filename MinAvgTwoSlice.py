def solution(A):
    # write your code in Python 3.6
    n = len(A)
    p = [0] * (n+1)
    min_averages = []
    for i in range(1, n+1):
        p[i] = p[i-1] + A[i-1]
        print('p'+str(i) + ' '+ str(p[i]))
    for i in range(n-1):
        averages = [(p[j] - p[i])/(j-i+1) for j in range(i+1,n+1)]
        print(averages)
        min_averages.append(min(averages))
        print(min_averages)
        print()
    return min_averages.index(min(min_averages))