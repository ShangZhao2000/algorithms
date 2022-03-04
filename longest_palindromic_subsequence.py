def longest_palindromic_subsequence(string):
    @lru_cache(None)
    def dp(i, j):
        if j < i:
            return 0
        if i == j:
            return 1
        if string[i] == string[j]:
            return 2 + dp(i + 1, j - 1)
        else:
            return max(dp(i + 1, j), dp(i, j - 1))
    return dp(0, len(string) - 1)

print(longest_palindromic_subsequence())