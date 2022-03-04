def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                i -= 1
            else:
                break
    return lst

print(insertion_sort([39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]))

def insertion_sort_2(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        while temp < lst[i - 1] and i > 0:
            lst[i] = lst[i - 1]
            i -= 1
        lst[i] = temp
    return lst

print(insertion_sort_2([39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]))