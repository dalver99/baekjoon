n = int(input())

sequence = [int(input()) for _ in range(n)]

orderlist = list()
for i in range (n):
    orderlist.append(int(i)+1)

#스택
reallist = list()

#결과저장
resultslist = list()

for k in range (n):
    num = sequence[k]
    if len(reallist) == 0:
        reallist.append(orderlist.pop(0))
        resultslist.append('+')

    if reallist.count(num) == 1 and reallist[-1] != num:
        resultslist.append(-1)

    if reallist[-1] != num and orderlist.count(num) != 0:
        #꺼낼준비를 해야한다
        while reallist[-1] != num:
            reallist.append(orderlist.pop(0))
            resultslist.append('+')
    if reallist[-1] == num:
        reallist.pop(-1)
        resultslist.append('-')
    
if resultslist.count(-1) != 1:
    for results in resultslist:
        print (results)
else:
    print('NO')