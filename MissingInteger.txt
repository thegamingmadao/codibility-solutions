def minpositive(A):
    a = set(A) # create a set of list A, this omits all duplicates
    n = 1 #n can be 1-100000
    # While n is in set a , increment n by 1 , this will exit when n is not found in a 
	while n in a:
       n += 1
    return n