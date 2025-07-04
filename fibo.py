def fibonacci(n):
    """Generate the first n Fibonacci numbers"""
    fib_sequence = [0, 1]  # Initialize with first two Fibonacci numbers
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]  # Sum of last two numbers
        fib_sequence.append(next_num)
    
    return fib_sequence

# printing
print(fibonacci(10))  # Prints first 10 Fibonacci numbers