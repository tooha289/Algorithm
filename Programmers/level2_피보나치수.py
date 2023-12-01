def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def solution(n):
    if n<=1:
        return n
    first = 0
    second = 1
    next = 0
    
    for i in range(n-1):
        next = first + second
        first = second
        second = next
    
    return next % 1234567