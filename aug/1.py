# fibonacci series

x = int(input("enter till how many numbers you want fibonacci series = "))
def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("invalid value enter a valid one!")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):  # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a+b
            a = b
            b = c
            if c > 100:
                break
            print(c)

fibo(x)