def coin_change_top_down(coins, amount):
    memo = [None for _ in range(amount + 1)]
    def dp(target):
        if target < 0:
            return float('inf')
        if target == 0:
            return 0
        if memo[target] is not None:
            return memo[target]
        else:
            optimum = 1 + min(dp(target - i) for i in coins)
            memo[target] = optimum
            return optimum
    return dp(amount)

def coin_change_bottom_up(coins, amount):
    dp = [0] + [float('inf') for _ in range(amount)]
    for i in range(1, amount + 1):
        dp[i] = 1 + min(dp[i - j] if i - j >= 0 else float('inf') for j in coins)
    return dp[-1]

