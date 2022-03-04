def kmp(string):
    arr = [0 for _ in range(len(string))]
    j = 0
    for i in range(1, len(arr)):
        while string[i] != string[j] and j > 0:
            j = arr[j - 1]
        if string[i] == string[j]:
            arr[i] = j + 1
            j += 1
        else:
            arr[i] = j
    return arr

print(kmp("bba"))