def solution(X, Y, D):
    # write your code in Python 3.6
    if (Y-X) % D:
        return (Y-X) // D + 1
    else:
        return (Y-X) // D