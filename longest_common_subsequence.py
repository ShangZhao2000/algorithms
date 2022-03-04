from functools import lru_cache
def longest_common_subsequence(str1, str2):
    @lru_cache(None)
    def dp(i, j):
        if i < 0:
            return 0
        if j < 0:
            return 0
        if str1[i] == str2[j]:
            return 1 + dp(i - 1, j - 1)
        else:
            return max(dp(i - 1, j), dp(i, j - 1))
    length = dp(len(str1) - 1, len(str2) - 1)
    LCS = []
    def reconstruct_solution(i, j):
        if i < 0 or j < 0:
            return
        if str1[i] == str2[j]:
            LCS.append(str1[i])
            reconstruct_solution(i - 1, j - 1)
        elif dp(i - 1, j) > dp(i, j - 1):
            reconstruct_solution(i - 1, j)
        else:
            reconstruct_solution(i, j - 1)
    reconstruct_solution(len(str1) - 1, len(str2) - 1)
    return "".join(LCS)[::-1]

string1 = "abac"
string2 = "cab"
print(longest_common_subsequence(string1, string2))