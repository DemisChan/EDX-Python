b0 = balance
apr = annualInterestRate
def fmp(b0, apr):
    '''
    fixed monthly payments
    '''
    mpr = apr/12
    a = mpr*(1+mpr)**12
    b = (1+mpr)**12-1
    c1 = a*b0/b
    #print(c1)
    c = c1 + (-c1) % 10
    #print(c)
    if c-c1 >= 5 and c1 > 10:
        print('Lowest payment:', c-10)
    elif c1 < 5:
        print('Lowest payment:', c)
    elif c-c1 <= 5:
        print('Lowest payment:', c)

fmp(b0, apr)
