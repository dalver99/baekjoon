count = [0] * 10001
import sys
input = sys.stdin.readline
N = int(input())

for _ in range (N):
    number = int(input())
    count[number] += 1

for i in range (1,10001):
    for j in range (count[i]):
        print(i)


"""
1\N > int(1\N) = 1
string

alpha\N = alpha\N
strip(alpha\N) = alpha
"""