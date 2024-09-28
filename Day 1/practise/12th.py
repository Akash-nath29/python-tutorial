#python program to print Fibonacci series up to n terms

def fibonacci_series(n):
    a, b = 0, 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a, end=" ")
            a, b = b, a + b
            count += 1

limit = int(input("Enter the limit of the range: "))
fibonacci_series(limit)
