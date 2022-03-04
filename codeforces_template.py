def solve(case_no):
    n = int(input())
    arr = list(map(int, input().strip().split())) #input in form 1 2 3
    ans = 0
    return "Case #" + str(case_no) + ": " + str(ans)

t = int(input())
for n in range(t):
    print(solve(n + 1))

def solve(case_no):
    n, m = list(map(int, input().strip().split()))
    n, m = int(n), int(m)
    a = list(map(int, input().strip().split())) #input in form 1 2 3
    special = int(input())
    num_idx = {a[i]:i for i in range(len(a))}
    def play(num, move):
    	if move > m:
    		return True
    	elif num in num_idx:
    		i = num_idx[num]
    		flag = False
    		for option in [
    	else:
    		return False
    return "Case #" + str(case_no) + ": " + str(ans)

print(solve())

from functools import lru_cache
# import time

n = int(input())
a = list(map(int, input().strip().split()))


best = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        best[i] = max(best[i], best[i - j] + a[j - 1])


@lru_cache(None)
def dp(i, j, e=0, o=0):
    if i == j or all(a[k] % 2 == a[k - 1] % 2 for k in range(i + 1, j + 1)):
        cnt = j - i + 1
        return best[cnt + e] + best[o] if a[i] % 2 == 0 else best[cnt + o] + best[e]

    ans = 0
    for k in range(i, j):
        ans = max(ans, dp(i, k, e, o) + dp(k + 1, j, 0, 0))
        ans = max(ans, dp(i, k, 0, 0) + dp(k + 1, j, e, o))

    if a[i] % 2 != a[j] % 2:
        return ans

    cnt = 0

    i0 = i
    while a[i0] % 2 == a[i] % 2:
        cnt += 1
        i0 += 1

    j0 = j
    while a[j0] % 2 == a[j] % 2:
        cnt += 1
        j0 -= 1
    
    if a[i] % 2 == 0:
        ans = max(ans, dp(i0, j0, e + cnt, 0) + best[o])
    else:
        ans = max(ans, dp(i0, j0, 0, o + cnt) + best[e])
    return ans


# start = time.time()
print(dp(0, n - 1))
# print(time.time() - start)

input().strip().split()

