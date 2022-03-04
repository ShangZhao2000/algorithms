def binary_representation(n):
    res = ["1" if n & 1 << i != 0 else "0" for i in range(30, -1, -1)]
    return int("".join(res))

print(binary_representation(2135))
