def fib(n):
    if n<=2:
        return 1
    else:
        a=1
        b=1
        for i in range(n-2):
            sub=a+b
            a=b
            b=sub
        return b

print(fib(10))