from functools import lru_cache
def longest_common_substring(str1, str2):
    @lru_cache(None)
    def dp(i, j):
        if i < 0 or j < 0:
            return 0
        if str1[i] == str2[j]:
            return 1 + dp(i - 1, j - 1)
        else:
            return 0
    len_pos = [0, 0]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if dp(i, j) > len_pos[0]:
                len_pos[0], len_pos[1] = dp(i, j), i
    return str1[len_pos[1] + 1 - len_pos[0] :len_pos[1] + 1]

string1, string2 = "abcdgh", "acdghrx"
print(longest_common_substring(string1, string2))