import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N,M = map(int,input().split())

dosi = []
chickenindexes = []
houseindexes = []

for i in range (N):
    row = list(map(int,input().split()))
    for idx,els in enumerate(row):
        if els == 2:
            chickenindexes.append((idx,i)) #holds (x,y) of index
        if els == 1:
            houseindexes.append((idx,i)) #holds (x,y) of index
    dosi.append(row)

# print(chickenindexes) 
# print(houseindex)
# print(dosi)

distancetable = [[-1]*len(houseindexes) for _ in range (len(chickenindexes))]
#가로가 chickenindex

# 그냥 각 집 위치별, 치킨집 위치별 거리를 싹 다 계산해두고, 치킨집을 선택한 뒤, 그떄그떄 최소값을 가져와서 더한 다음, 그 최소값의 합의 최소를 구하자.

for idx,(housex,housey) in enumerate(houseindexes):
    for idxx,(chickenx,chickeny) in enumerate(chickenindexes):
        distancetable[idxx][idx] = abs(chickenx-housex) + abs(chickeny-housey)
#print(distancetable)

#distancetable[B][A]에는 집 A에서 치킨집 B까지의 거리가 저장되어있음

indexes = [i for i in range(len(chickenindexes))]
combs = combinations(indexes,M)

distance = 9999999
for comb in combs: #치킨집의 인덱스의 집합이 선택됨.
    tempdistance = 0
    findfrom = []
    for eachindex in comb: #각 인덱스에 대해
        #distancetable에서 그 열을 뽑아내버려.
        row = distancetable[eachindex]
        findfrom.append(row)
    #print(findfrom)
    #[[2, 2, 2, 5, 6, 6], [5, 7, 5, 2, 1, 1]] 여기서 222211 선택하면 그만!
    for idx in range(len(houseindexes)):
        tempdistance += min(row[idx] for row in findfrom)
    
    distance = min(distance,tempdistance)

print(distance)
    
# chickendistances = []

# combs = combinations(chickenindexes,M)
# distance = 999999
# for comb in combs: #이걸 다 해보자 .......
#     tempdistance = 0
#     for housex,housey in houseindexes: #집 좌표 하나씩
#         #각 집에서 거리계산 다해보기 #진짜 비효율적인 건 나도 알고 있음.
#         for chickenx,chickeny in comb: #(1,0), (0,3)
#             tempdistance += abs(chickenx-housex) + abs(chickeny-housey)
#     distance = min(tempdistance,distance)

# print(distance)

# # for house in houseindexes:
# #     housex,housey = house
# #     temp = 99
# #     for chicken in chickenindexes:
# #         chickenx,chickeny = chicken
# #         temp = min(temp,(abs(chickenx-housex)+abs(chickeny-housey)))

# # print(chickendistances)