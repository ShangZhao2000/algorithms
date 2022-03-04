from factorial_representation import factorial_representation
def kth_smallest_permutation(k, string):
    string = sorted(string)
    res = []
    x = factorial_representation(k)
    for i in x:
        res.append(string[int(i)])
        string = string[:int(i)] + string[int(i) + 1:]
    return "".join(res)
print(kth_smallest_permutation(14, "badc"))