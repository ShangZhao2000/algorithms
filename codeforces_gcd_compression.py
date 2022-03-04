def gcd_compression():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    even_lst = []
    odd_lst = []
    for i in range(2*n):
        if lst[i] % 2 == 0:
            even_lst.append(i + 1)
        else:
            odd_lst.append(i + 1)
    if len(odd_lst) != 0:
        if len(odd_lst) % 2 == 0:
            odd_lst.pop()
        else:
            even_lst.pop()
        odd_lst.pop()
    else:
        even_lst.pop()
        even_lst.pop()
    for i in range(0, len(even_lst) - 1, 2):
        print(str(even_lst[i]) + " " + str(even_lst[i + 1]))
    for i in range(0, len(odd_lst) - 1, 2):
        print(str(odd_lst[i]) + " " + str(odd_lst[i + 1]))
    
    

t = int(input())
for _ in range(t):
    gcd_compression()