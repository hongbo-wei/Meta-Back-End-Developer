# recursion
def fibonacci(n):
    '''
    n: integer
    '''
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Example usage:
n = 10
print(fibonacci(n))  # Output: 55