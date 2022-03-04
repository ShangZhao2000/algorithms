def longest_palindromic_substring_dp(string):
    @lru_cache(None)
    def dp(i, j):
        if i >= j:
            return 1
        if string[i] == string[j]:
            return 1 if dp(i + 1, j - 1) == 1 else 0
        else:
            return 0
    mmax = 0
    start, end = None, None
    for i in range(len(string)):
        for j in range(i, len(string)):
            if dp(i, j) and j - i + 1 > mmax:
                mmax = j - i + 1
                start, end = i, j
    return string[start: end + 1]

def longest_palindromic_substring_manacher(string):
    t = "#".join("%{}&".format(string))
    palindrome_lengths = [0 for _ in range(len(t))]
    c, r = 0, 0
    for i in range(1, len(t) - 1):
        if i < r:
            palindrome_lengths[i] = min(r - i, palindrome_lengths[2 * c - i])
        else:
            palindrome_lengths[i] = 0
        while t[i + 1 + palindrome_lengths[i]] == t[i - 1 - palindrome_lengths[i]]:
            palindrome_lengths[i] += 1
        if i + palindrome_lengths[i] > r:
            c, r = i, i + palindrome_lengths[i]
    length, idx = max((palindrome_lengths[i], i) for i in range(len(palindrome_lengths)))
    return string[(idx - length) // 2: (idx + length) // 2]
