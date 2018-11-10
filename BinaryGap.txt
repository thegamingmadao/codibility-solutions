def solution(N):
    #Convert to binary, slice past the first 2 chars, strip 0s left and right
	xs = bin(N)[2:].strip('0').split('1') # Split in empty substrings and substrings of 0s
    return max([len(x) for x in xs])