n = int(input())
S = []

def add(val):
    S.append(val)

def remove(val):
    if S.count(val) != 0:
        S.remove(val)

def check(val):
    if S.count(val) == 0:
        print('0')
    else:
        print('1')

def toggle(val):
    if S.count(val) == 0:
        S.append(val)
    else:
        S.remove(val)

def all():
    global S
    S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def empty():
    global S
    S = []


for _ in range (n):
    string = input()

    if string == 'all':
        all()
    elif string == 'empty':
        empty()
    else:   
        order, val = map(str,string.split())
        val = int(val)
        if order == 'check':
            check(val)
        elif order == 'remove':
            remove(val)   
        elif order == 'add':
            add(val)   
        elif order == 'toggle':
            toggle(val)