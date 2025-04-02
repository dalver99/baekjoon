import sys
input = sys.stdin.readline
N = int(input())
for _ in range (N):
    ps = input().strip()
    while len(ps)>1:
        if '()' in ps:
            ps = ps.replace("()","")
            # print(ps)
        else:
            break
    if ps == "":
        print('YES')
    else:
        print('NO')


