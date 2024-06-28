import sys
import math

def distance(x1,y1,x2,y2): 
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = distance(x1,y1,x2,y2)
        res = 0
       # print('dist' + str(d))

        #CASE 0 두 점이 같은 경우
        if d == 0:
            if r1==r2:
                res = -1
        #CASE 1 그래도 겹친 경우
        elif abs(r1-r2) < d < (r1+r2):
            res = 2
        #CASE 2 한점 겹친 경우
        elif abs(r1-r2) == d or r1+r2 == d:
            res = 1
        else:
            res = 0

        print(res)
        # sys.stdout.write(str(res))


if __name__ == '__main__':
    main()