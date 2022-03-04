def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    else:
        m = n//2
        res = []
        left, right = merge_sort(lst[:m]), merge_sort(lst[m:])
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            elif right[0] < left[0]:
                res.append(right.pop(0))
            elif left[0] == right[0]:
                res.append(left.pop(0))
                res.append(right.pop(0))
        res.extend(left)
        res.extend(right)
        return res

print(merge_sort([39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]))