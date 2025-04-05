import sys
sqs = []
from itertools import permutations
target = int(input())
for i in range (1,3): #223*223 = 49729
    sqs.append(i**2)

#
for a,b in permutations(sqs,2):
    print(a,b)