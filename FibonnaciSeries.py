def fib(n):
    a = 0
    b = 1
    while a < n:
        a, b = b, a+b
        print(a)

inpString = input("Enter a number: ")
fib(int(inpString))




