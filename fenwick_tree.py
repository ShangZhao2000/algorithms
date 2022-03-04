from itertools import accumulate
class fenwick_tree:
    def __init__(self, arr):
        self.arr = arr
        self.presum = list(accumulate(self.arr))
        self.tree = [None for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            p_i = (i + 1) & -(i + 1)    #largest power of 2 that divides n is given by n & -n (or equivalently, n & (~(n - 1))). Code adjusted for 1 indexing.
            self.tree[i + 1] = self.presum[i] - (self.presum[i - p_i] if i - p_i >= 0 else 0)
    def range_sum(self, left, right):
        ssum1, ssum2 = 0, 0
        i, j = right, left - 1
        while i >= 1:
            ssum1 += self.tree[i]
            i -= i & -i
        while j >= 1:
            ssum2 += self.tree[j]
            j -= j & -j
        return ssum1 - ssum2
    def update_value(self, idx, new_val):
        old_val = self.arr[idx - 1]
        while idx <= len(self.tree) - 1:
            self.tree[idx] += new_val - old_val
            idx += idx & -idx
    def get_tree(self):
        return self.tree


tree = fenwick_tree([1, 3, 4, 8, 6, 1, 4, 2])
print(tree.get_tree())
print(tree.range_sum(1, 7))
