n = int(input())

for _ in range(n):
    error = False
    rev = False
    order = list(input()) # Rs and Ds
    arrnum = int(input()) # how many numbers?
    original = str(input().strip("[]")) # input
    numlist = original.split(',') # to list

    if arrnum == 0 and order.count('D'):
        error = True

    for i in range(len(order)):
        if order[i] == 'R':
            rev = not rev
        else: # if D
            if len(numlist) == 0:
                error = True
            else:
                if rev:
                    numlist.pop(-1)
                else:
                    numlist.pop(0)


    if not error:
        if rev:
            numlist.reverse()
        print('[', end='')
        for idx, number in enumerate(numlist):
            if idx != len(numlist) - 1:
                print(number, end=',')
            else:
                print(number, end='')
        print(']')
    else:
        print('error')