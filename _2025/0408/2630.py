import sys
def D(n):
    n*=2
    if n>9999:
        n%=10000
    return n

def S(n):
    n -= 1
    if n == 0:
        n=9999
    return n
    
def L(n):
    n = str(n).zfill(4)
    new = []
    new.append(n[1])
    new.append(n[2])
    new.append(n[3])
    new.append(n[0])
    n = int("".join(new))
    return n
    
def R(n):
    n = str(n).zfill(4)
    new = []
    new.append(n[3])
    new.append(n[0])
    new.append(n[1])
    new.append(n[2])
    n = int("".join(new))
    return n

print(D(6000))
print(L(1000))
print(S(1))
print(R(1))

input = sys.stdin.readline
T = int(input())

for _ in range (T):
    fromthis,tothis = map(int,input().split())
    