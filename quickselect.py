def quickselect(lst, k):
    """This needs to be fixed.
    
    """

    def kth_smallest_element(k, low, high):
        pivot_pos = partition(low, high)
        if pivot_pos == k - 1:
            return lst[pivot_pos]
        elif pivot_pos < k - 1:
            return kth_smallest_element(k - pivot_pos - 1, pivot_pos + 1, high)
        else:
            return kth_smallest_element(k, low, pivot_pos - 1)

    def partition(low, high):
        pivot = lst[low]
        l, r = low + 1, high
        while l < r:
            if lst[l] > pivot and lst[r] <= pivot:
                lst[l], lst[r] = lst[r], lst[l]
            if lst[l] <= pivot:
                l += 1
            if lst[r] > pivot:
                r -= 1
        if lst[r] <= pivot:
            lst[low], lst[r] = lst[r], lst[low]
            return r
        else:
            return low

    return kth_smallest_element(k, 0, len(lst) - 1)

lst1 = [4,8,6,4,2,4,1,7,3,4,5]
print(quickselect(lst1, 9))
print(sorted(lst1)[8])