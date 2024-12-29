n = int(input())
dolist = []
nlist = []
for k in range(n):
    dolist.append(int(input()))
    nlist.append(int(k+1))

reallist = []
printlist = []
while dolist:
    target = dolist.pop(0) # 4
    if nlist.count(target) == 1:
        idx = nlist.index(target)
        for i in range (idx+1):
#            print('+')
            printlist.append('+')
            reallist.append(nlist.pop(0))
    if reallist.count(target) == 1:
        if reallist[-1] == target:
#            print('-')
            printlist.append('-')
            reallist.remove(target)
        else:
            printlist.append('NO')
#            print('NO')
            break

if printlist.count('NO') == 1:
    print('NO')
else:
    for stuff in printlist:
        print(stuff)

