#You are given the following definitions:
# run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
#A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
#Implement a function that meets the specifications below. 


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    count = 0
    longest = 0
    result = 0
    count2 = 0
    longest2 = 0
    result2 = 0
    for i in range(len(L) - 1):
        if (L[i] <= L[i + 1]):
            count += 1
            if count > longest:
                longest = count
                result = i + 1
        else:
            count = 0
    startposition = result - longest
    li =L[startposition:result + 1]
    for i in range(len(L) - 1):
        if (L[i] >= L[i + 1]):
            count2 += 1
            if count2 > longest2:
                longest2 = count2
                result2 = i + 1
        else:
            count2 = 0
    startposition2 = result2 - longest2
    ld =L[startposition2:result2 + 1]
    if len(li) == len(ld) and startposition < startposition2:
        return sum(li)
    elif len(li) == len(ld) and startposition > startposition2:
        return sum(ld)
    elif len(li) > len(ld):
        return sum(li)
    elif len(li) < len(ld):
        return sum(ld)
    else:
        return sum(li) 
