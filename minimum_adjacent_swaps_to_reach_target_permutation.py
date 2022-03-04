def min_adjacent_swaps(arr, target):
    arr, target = list(arr), list(target)
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != target[i]:
            for j in range(i - 1, -1, -1):
                if arr[j] == target[i]:
                    count += i - j
                    break
            for k in range(j, i):
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return count

print(min_adjacent_swaps("5489355142", "5489355421"))