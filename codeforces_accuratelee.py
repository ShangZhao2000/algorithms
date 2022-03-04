def cleanest_string():
    n = int(input())
    s = str(input()).strip()
    if n == 1:
        print(s)
    else:
        for i in range(n):
            if s[i] != "0":
                break
        for j in range(n - 1, -1, -1):
            if s[j] != "1":
                break
        if i == 0 and j == 0:
            print(n * "1")
        elif j == n - 1 and i == n - 1:
            print(n * "0")
        elif i > j:
            print(i * "0" + (n - j - 1) * "1")
        else:
            print((i + 1) * "0" + (n - j - 1) * "1")

t = int(input())
for _ in range(t):
    cleanest_string()