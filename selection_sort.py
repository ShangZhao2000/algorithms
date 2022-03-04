def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        curr_min_index = i 
        for j in range(i + 1, n):
            if lst[j] < lst[curr_min_index]:
                curr_min_index = j
        lst[i], lst[curr_min_index] = lst[curr_min_index], lst[i]
    return lst

print(selection_sort([39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]))