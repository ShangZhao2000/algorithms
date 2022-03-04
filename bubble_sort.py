#def bubble_sort(lst):
#    changes=1
#    while changes!=0:
#        changes=0
#        for i in range(len(lst)-1):
#            if lst[i]>lst[i+1]:
#                lst[i],lst[i+1]=lst[i+1],lst[i]
#                changes+=1
#    return lst


def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def bubble_sort_2(lst):
    n = len(lst)
    for i in range(n - 1):
        changed = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                changed = True
        if not changed:
            break
    return lst




print(bubble_sort_2([39,23,70,19,35,64,97,15,22,31,38,42,69,76,98]))
    