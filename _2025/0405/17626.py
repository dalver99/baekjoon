import sys
sqs = []
from itertools import combinations_with_replacement
target = int(input())
for i in range (1,224): #223*223 = 49729
    sqs.append(i**2)

#one
for nums in sqs:
    if nums == target:
        print(1)
        sys.exit()

#two
for a,b in combinations_with_replacement(sqs,2):
    if a+b == target:
        print(2)
        sys.exit()

#three
for a,b,c in combinations_with_replacement(sqs,3):
    if a+b+c == target:
        print(3)
        sys.exit()

#four
print(4)