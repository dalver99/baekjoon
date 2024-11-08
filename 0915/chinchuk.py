import sys

intlist = []
anslist = []

N =  int(sys.stdin.readline())
for _ in range(N):
    intlist.append(int(sys.stdin.readline()))

intlistlen = len(intlist)

minint = int(min(intlist))

for i in range(minint):
    for ints in intlist:
        temp = ints % (i+1)
        if intlist[0] == ints:
            ans = temp
        if ans != temp:
            break
        if intlist[intlistlen-1] == ints and ans == temp:
            anslist.append(i+1)

print(' '.join(map(str,anslist)))
