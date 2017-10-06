def factorial(n):
    '''This function calculates the factorial of a number N.'''
    if n in (0, 1):
        return 1
    return factorial(n-1) * n

print(factorial(110))
