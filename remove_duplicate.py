def remove_duplicate(lst):
    j = 0
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            lst[j] = lst[i]
            j += 1
    lst[j] = lst[-1]
    for _ in range(len(lst) - j - 1):
        lst.pop()

lst1 = [2,2,2,2,2]
remove_duplicate(lst1)
print(lst1)

lst2 = [5,2,3,6,4,2,5,4,3,7,8,7,6,7,8,9,4,5,7,2]
remove_duplicate(lst2)
print(lst2)