# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 49 > 어떤 시점부턴 그냥 -4번째를 더한거네?
import sys
input = sys.stdin.readline

T = int(input())

Pn = [1,1,1,2,2,3,4,5,7,9,12,16,21,28]

# print(len(Pn))

for i in range (87):
    Pn.append(Pn[13+i] + Pn[9+i])

# print(Pn[14]) #37
# print(Pn[15]) #49

for _ in range (T):
    N = int(input())
    print(Pn[N-1])