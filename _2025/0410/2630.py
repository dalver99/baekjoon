import math
# import numpy as np

N = int(input())
power = int(math.log2(N)) + 1
paper = []
white = 0
blue = 0

for _ in range(N):
    row = list(map(int,input().split()))
    paper.append(row)

# arr = np.array(paper)

for i in reversed(range(power)): #8이면 2,1,0
    length = 2**i #4,2,1
    iteration = (N//length) #근데 마지막거는 그냥 sum으로 세도 된다.
    #2,4,8
    #4,16,64 #4배씩 늘어남
    for j in range (iteration):
        for k in range (iteration):
            #2x2 사각형을 센다고 생각하고 계산
            #00,01,02,03,10,11,12,13, ... 
            #iteration = 4
            #index의 범위는
            #00~11, 02~13, 04~15, 06~17 // 20~31, .. 
            #k*length,j*length ~ k*length+1,j*length+1

            # square = arr[k*length:k*length+(length),j*length:j*length+(length)]
            # #print(square)
            # if square.sum() == length**2:
            #     arr[k*length:k*length+(length),j*length:j*length+(length)] = -55
            #     blue += 1
            # if square.sum() == 0:
            #     arr[k*length:k*length+(length),j*length:j*length+(length)] = -55
            #     white += 1

#넘파이를 없애라
            start_x = k * length
            start_y = j * length
            uniform = True
            base_color = paper[start_x][start_y]
            for x in range(start_x, start_x + length):
                for y in range(start_y, start_y + length):
                    if paper[x][y] != base_color:
                        uniform = False
                        break   
                if not uniform:
                    break
            if uniform:
                for x in range(start_x, start_x + length):
                    for y in range(start_y, start_y + length):
                        paper[x][y] = -1
                if base_color == 0:
                    white += 1
                elif base_color == 1:
                    blue += 1


print(white)
print(blue)
                
