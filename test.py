print("Hell world")
# Implement Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
    print()
fibonacci(10)

# Reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello World"))


