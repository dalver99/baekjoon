import sys
input = sys.stdin.readline

def perform_op(S, op, x=None):
    if op == 'add':
        S.add(x)
    elif op == 'remove':
        S.discard(x)  # discard method does not raise an error if element does not exist
    elif op == 'check':
        print(1 if x in S else 0)
    elif op == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif op == 'all':
        S = set(range(1, 21))  # oh shit
    elif op == 'empty':
        S.clear()  
    return S

M = int(input())
S = set()

for _ in range(M):
    command = input().strip().split()
    if len(command) == 1:
        op = command[0]
        S = perform_op(S, op)
    else:
        op, x = command[0], int(command[1])
        S = perform_op(S, op, x)