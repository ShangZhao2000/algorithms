def partition(lst):
    left, curr, right = 0, 1, len(lst) - 1
    pivot = lst[0]
    while curr < right:
        if lst[curr] < pivot:
            lst[left], lst[curr] = lst[curr], lst[left]
            left += 1
            curr += 1
        elif lst[curr] > pivot:
            lst[curr], lst[right] = lst[right], lst[curr]
            right -= 1
        else:
            curr += 1
    return lst

print(partition([4,8,6,4,2,4,1,7,3,4,5]))