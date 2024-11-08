import math
n = int(input())
fact = math.factorial(n)
k = 0
while True:
    if fact%10 == 0:
        k += 1
        fact /= 10
    if fact%10 != 0:
        break


print(int(k))

#gives overflow error, try something new