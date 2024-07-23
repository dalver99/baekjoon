n = int(input())

sequence = [int(input()) for _ in range(n)]

orderlist = list()
for i in range (n):
    orderlist.append(int(i)+1)

#진짜 시작한다
reallist = list()
reallist.append(1)
#결과저장
resultslist = list()
resultslist.append('+')
orderlist.remove(1)

for k in range (n):
    num = sequence[k]
#    print('for num: '+ str(num))
 #   print('resultslist: ' + str(resultslist))
  #  print('reallist: ' + str(reallist))
   # print('orderlist: ' + str(orderlist))

    # if orderlist.count(num) == 0 and reallist.count(num) == 0:
    #     #impossible
    #     print('NO')
    #     resultslist.append(-1)
    #     break
    if orderlist.count(num) == 1 or reallist.count(num) == 1:
        if len(reallist) >= 1:
            while reallist[-1] != num:
                #print('더 넣어!')
                if orderlist.count(num) == 0:
                    print('NO')
                    break

                reallist.append(orderlist.pop(0))
                resultslist.append('+')
                # 맞넹
            if reallist[-1] == num:
                reallist.pop(-1)
                resultslist.append('-')

if resultslist.count(-1) != 1:
    for results in resultslist:
        print (results)

#print('resultslist: ' + str(resultslist))
#print('reallist: ' + str(reallist))
#print('orderlist: ' + str(orderlist))