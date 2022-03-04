def counting_sort(lst):
    bins = [[] for _ in range(max(lst) + 1)]
    for i in lst:
        bins[i].append(i)
    lst = []
    for i in bins:
        lst.extend(i)
    return lst
