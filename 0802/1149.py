N = int(input())

# 밑에있는애가 위에있는애를 고르는 개념으로 접근
# 계속 3가지 옵션 뿐임

rgb = list(map(int,input().split()))
costr = rgb[0]
costg = rgb[1]
costb = rgb[2]

for _ in range (N-1):
    rgb = list(map(int,input().split()))
    tempr = rgb[0] +min(costg,costb)
    tempg = rgb[1] +min(costr,costb)
    tempb = rgb[2] +min(costg,costr)
    costr = tempr
    costg = tempg
    costb = tempb

print(min(costr,costg,costb))