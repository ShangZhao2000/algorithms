from functools import lru_cache
import bisect
def longest_increasing_subsequence_1(lst):
    """
    @Complexity: O(n^2)
    """
    @lru_cache(None)
    def dp(i):
        if i == 0:
            return 1
        else:
            return 1 + max(dp(j) if lst[i] > lst[j] else 0 for j in range(i))
    return max(dp(i) for i in range(len(lst)))

def longest_increasing_subsequence_2(lst):
    """
    @Complexity: O(nlog(n))
    """
    arr = []
    for i in lst:
        pos = bisect.bisect_left(arr, i)
        if pos == len(arr):
            arr.append(i)
        else:
            arr[pos] = i
    return len(arr)

x = [3,4,-1,5,8,2,3,12,7,9,10]
print(longest_increasing_subsequence_1(x))
print(longest_increasing_subsequence_2(x))