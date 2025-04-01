from collections import deque
import sys

input = sys.stdin.readline
TC = int(input())
for _ in range (TC):
    printed = -1
    printn = 0
    N,M = map(int,input().split())
    que = list(map(int,input().split()))
    realque = []
    for i in range(N):
        realque.append([que[i],i])
    #print(realque)
    while printed != M:
        importancesort = sorted(realque, key=lambda x: x[0])
        maximportance = importancesort[-1][0]
        #print("maximp: "+str(maximportance))
        
        item,idx = realque.pop(0)
        #print("poped: "+str(item)+"with idx"+str(idx))
        
        if item == maximportance:
        
            printed = idx
            #print("printed: "+str(item))
            printn += 1
        else:
            realque.append([item,idx])

    print(printn)