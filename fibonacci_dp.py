def aux(n, memo):
    if memo[n]!=-1:
        return memo[n]
    else:
        memo[n]=aux(n-1, memo)+aux(n-2, memo)
        return memo[n]

def fib(n):
    memo=[0,1,1]+(n-2)*[-1]
    return aux(n, memo)

print(fib(500))

