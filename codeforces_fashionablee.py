def solve():
    n = int(input())
    if n % 4 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()