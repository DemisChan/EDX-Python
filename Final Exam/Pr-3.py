def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    x = list(s.lstrip())
    l = 0
    count = 0
    for i in x:
        try:
            l += int(i)
            count += 1
        except ValueError:
            continue
    if count == 0:
        raise ValueError
    else:
        return l
