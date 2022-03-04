def factorial_representation(num):
    s = []
    divisor = 1
    while True:
        num, mod = divmod(num, divisor)
        s.append(str(mod))
        divisor += 1
        if num == 0:
            break
    return "".join(s[::-1])

#print(factorial_representation(349))