def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
    """
    x = L[:]
    L.clear()
    for i in range(len(x), 0, -1):
        L.append(x[i-1][::-1])
    return L
