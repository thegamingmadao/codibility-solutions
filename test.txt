def solution(S, P, Q):
	#length of Q and P queries
	q = len(q)
	#Length of string
	s = len(S)
	#Empty string to store the return values
	results = []
	#Temporary variable
	tmp = ''
	#Initialization of list p to store prefix sums of chars in strings S
	p=['']*(n+1)
	#Storing the value of each prefix
	for k in range(1, n+1):
        p[k] = p[k-1] + S[k-1]
	for i in range(q):
		tmp = p[Q[q]].replace(p[P[q]],'')
		if 'A' in tmp:
			results.append(1)
		elif 'C' in tmp:
			results.append(2)
		elif 'G' in tmp:
			results.append(3)
		elif 'T' in tmp:
			results.append(4)
	return results
		