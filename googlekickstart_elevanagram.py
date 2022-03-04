from functools import lru_cache
def solve():
    lst = list(map(int, input().strip().split()))
    arr = []
    for i in range(len(lst)):
        for j in range(lst[i]):
            arr.append(i + 1)
    tally = 0
    total_nums = len(arr)
    neg = total_nums // 2
    pos = total_nums - neg
    
    @lru_cache(None)
    def dp(i, pos, neg, tally):
        if i >= len(arr):
            return tally % 11 == 0
        else:
            res1 = False
            res2 = False
            if neg:
                res1 = dp(i + 1, pos, neg - 1, tally - arr[i])
            if pos:
                res2 = dp(i + 1, pos - 1, neg, tally + arr[i])
            return res1 or res2
    return dp(0, pos, neg, tally)
    

t = int(input())
for i in range(t):
    res = "YES" if solve() else "NO"
    print("Case #" + str(i + 1) + ": " + res)
    