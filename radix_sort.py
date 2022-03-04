def radix_sort(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    
    max_len = max(len(i) for i in lst)
    bins = [[] for i in range(10)]

    for i in range(1, max_len+1):
        for j in lst:
            try:
                bins[int(j[-i])].append(j)
            except IndexError:
                bins[0].append(j)
        lst = []
        for k in range(10):
            lst.extend(bins[k])
            bins[k]=[]

    return lst

print(radix_sort([39,23,70,19,35,64,97,15,22,31,38,420,69,76,98]))
        