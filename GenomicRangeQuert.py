def solution(S, P, Q):
    #length of Q and P queries
    q = len(Q)
    #Length of string
    s = len(S)
    #Empty string to store the return values
    results = []
    #Temporary variable
    tmp = ''
    #Initialization of list p to store prefix sums of chars in strings S
    p = [''] * (s+1)
    #Storing the value of each prefix sum
    for i in range(1, s+1):
        p[i] = p[i-1] + S[i-1]
    #Finding the chars between pairs of Q and P, Q+1 - P to include all chars specified
    for i in range(q):
        #using max = 1 to avoid replacing random occurences
        tmp = p[Q[i]+1].replace(p[P[i]],'', 1) 
        #If statement to store in results the min value of tmp
        if 'A' in tmp:
            results.append(1)
        elif 'C' in tmp:
            results.append(2)
        elif 'G' in tmp:
            results.append(3)
        elif 'T' in tmp:
            results.append(4)
    return results