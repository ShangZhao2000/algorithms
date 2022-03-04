def partition(lst, left, right):
    pivot_index = left
    swap_pos = pivot_index + 1
    i = swap_pos
    while i < right:
        i += 1
        if lst[swap_pos] < lst[pivot_index]:
            swap_pos += 1
        elif lst[i] < lst[pivot_index]:
            lst[swap_pos], lst[i] = lst[i], lst[swap_pos]
    if lst[swap_pos] < lst[pivot_index]:
        lst[swap_pos], lst[pivot_index] = lst[pivot_index], lst[swap_pos]
        return swap_pos
    else:
        lst[swap_pos - 1], lst[pivot_index] = lst[pivot_index], lst[swap_pos - 1]
        return swap_pos - 1

def aux(lst, left, right):
    if right > left:
        aux(lst, left, partition(lst, left, right) - 1)
        aux(lst, partition(lst, left, right) + 1, right)

def quicksort(lst):
    return aux(lst, 0, len(lst) - 1)

unsorted_list1 = [39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]
unsorted_list2 = [2,2,2,2,2,3,2,2,2]
unsorted_list3 = [3,2,6,76,8,7,4,9,54,34,70,65,90,32]
unsorted_list4 = [4,5,3,2,1,9,8,7,5,6,4,5,3,8,6,9,6,5,7,5]
quicksort(unsorted_list4)
print(unsorted_list4)