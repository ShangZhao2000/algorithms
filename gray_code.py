def sequence(n):
    res = []
    for i in range(n):
        res.append(i ^ (i >> 1))
    return res

print(sequence(16))