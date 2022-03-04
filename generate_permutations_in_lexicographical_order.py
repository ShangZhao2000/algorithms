import math
def generate_permutations(lst):
    permutations = []
    permutations.append(lst)
    limit = math.factorial(len(lst))
    for _ in range(limit - 1):
        curr = permutations[-1][:]
        for i in range(len(curr) - 2, -1, -1):
            if curr[i] < curr[i + 1]:
                break
        for j in range(len(curr) - 1, i, -1):
            if curr[j] > curr[i]:
                break
        curr[i], curr[j] = curr[j], curr[i]
        curr[i + 1:] = curr[i + 1:][::-1]
        permutations.append(curr)
    return permutations

res = generate_permutations([1,2,3,4])
print(res)
for i in range(1, len(res)):
    if res[i] < res[i - 1]:
        print(False)
        break
print(True)