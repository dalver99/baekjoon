import sys

i = int(sys.stdin.readline())

for _ in range(i):
    w,h,n = map(int,input().split())
    
    floor = n%w
    if floor == 0:
        floor = w

    num = int(n/w)
    if n%w != 0:
        num += 1

    room = floor*100 + num
    sys.stdout.write(str(room)+'\n')