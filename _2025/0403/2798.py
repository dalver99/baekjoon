from itertools import combinations 
N,M = map(int,input().split())
cards = map(int,input().split())

closest = -1
absdiff = 999999999

for each_comb in combinations(cards,3):
    ssum = sum(each_comb)
    diff = abs(ssum - M)
    if ssum <= M and diff < absdiff:
        absdiff = diff
        closest = ssum

print(closest)

