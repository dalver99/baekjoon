n = int(input())


def fibo(n):
    # print('called for ' + str(n))
    global Z,O
    if n == 0:
        Z += 1
    elif n == 1:
        O += 1
    else:
        fibo(n-1)
        fibo(n-2)


for _ in range (n):
    num = int(input())
    Z = 0
    O = 0
    fibo(num)
    print('{} {}'.format(Z,O))