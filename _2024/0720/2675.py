n = int(input())

for _ in range(n):
    rep, string = map(str,input().strip().split())
    lst = list(string)
    for k in range(len(lst)):
        for _ in range (int(rep)):
            print(lst[k], end='')
    print('')
