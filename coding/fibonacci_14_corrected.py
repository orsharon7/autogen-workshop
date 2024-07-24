# filename: fibonacci_14_corrected.py

def fibonacci(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Calculate the 14th Fibonacci number starting with F(0) = 0, F(1) = 1
fib_14 = fibonacci(14)
print(f"The 14th Fibonacci number is: {fib_14}")