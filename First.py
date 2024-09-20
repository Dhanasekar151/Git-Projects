def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fibonacci(10):
    print(i)
"""
This function prints the first n fibonacci numbers

Example:
    >>> fibonacci(10)
    0 1 1 2 3 5 8 13 21 34
"""
# Completed
