from functools import lru_cache
def salesman_top_down(lst):
    @lru_cache(None)
    def dp(i):
        if i == len(lst) - 1:
            return lst[-1]
        if i > len(lst) - 1:
            return 0
        else:
            return max(lst[i] + dp(i + 2), dp(i + 1))
    return dp(0)

def salesman_bottom_up(lst):
    if not lst:
        return 0
    if len(lst) < 3:
        return max(lst)
    else:
        dp = [lst[0], max(lst[0], lst[1])]
        for i in range(2, len(lst)):
            dp[0], dp[1] = dp[1], max(dp[0] + lst[i], dp[1])
        return dp[-1]

