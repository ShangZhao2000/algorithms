def partition(lst):
    pivot = lst[0]
    l, r = 1, len(lst) - 1
    while l < r:
        if lst[l] > pivot and lst[r] <= pivot:
            lst[l], lst[r] = lst[r], lst[l]
        if lst[l] <= pivot:
            l += 1
        if lst[r] > pivot:
            r -= 1
    lst[0], lst[r] = lst[r], lst[0]
    return lst

print(partition([4,8,6,2,1,7,3,5]))