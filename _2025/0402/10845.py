import sys
input = sys.stdin.readline
N = int(input())
q = []

for _ in range (N):
    order = input().strip()
    if order[0:2] == 'pu':
        # print(order[-1])
        q.append(order.split()[1])
    elif order[0:2] == 'po':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif order[0:2] == 'si':
        print(len(q))
    elif order[0:2] == 'em':
        print(1 if len(q) == 0 else 0)
    elif order[0:2] == 'fr':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0:2] == 'ba':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])