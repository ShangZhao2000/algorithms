import math

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def number_game():
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n % 2 == 0 and n != 2:
        ok = True
        u = n
        while u > 1:
            if u % 2 == 1:
                ok = False
                break
            u = u//2
        if ok:
            print("FastestFinger")
        else:
            n = n//2
            if n % 2 == 0:
                print("Ashishgup")
            else:
                prime = is_prime(n)
                if prime:
                    print("FastestFinger")
                else:
                    print("Ashishgup")
    else:
        print("Ashishgup")
        


t = int(input())
for _ in range(t):
    number_game()