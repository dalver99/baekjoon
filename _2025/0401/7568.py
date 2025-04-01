# import sys
# input = sys.stdin.readline

# N = int(input())
# all = []
# for i in range (N):
#     x,y = map(int,input().split())
#     all.append([x,y,i])

# xtheny = sorted(all ,key=lambda x:(x[0],x[1]),reverse=True)
# ranknumbers = [0] * N
# ranknumber = 1
# temp = 0
# tempx = xtheny[0][0]
# tempy = xtheny[0][1]

# for i in range(len(xtheny)):
#     if xtheny[i][0] < tempx and xtheny[i][1] < tempy:
#         #another ranking!
#         ranknumber += temp
#         temp = 1
#     else:
#         temp += 1

#     tempx, tempy = xtheny[i][0], xtheny[i][1]
#     ranknumbers[xtheny[i][2]] = ranknumber 

# print(*ranknumbers)

N = int(input())
all = [tuple(map(int, input().split())) for _ in range(N)]

ranks = [1] * N  # Start everyone at rank 1

for i in range(N):
    for j in range(N):
        if i != j:
            if all[i][0] < all[j][0] and all[i][1] < all[j][1]:
                ranks[i] += 1

print(*ranks)