print("Hell world")
# Implement Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
    print()
fibonacci(10)

