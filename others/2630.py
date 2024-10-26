import math

n = int(input())
sq = []
for i in range(n):
    row = list(map(int,(input().split())))
    sq.append(row)

def all_elements_are_one(matrix):
    for row in matrix:
        for element in row:
            if element != 1:
                return False
    return True

def all_elements_are_zero(matrix):
    for row in matrix:
        for element in row:
            if element != 0:
                return False
    return True

cuts = int(math.log2(n)) # n이 2면, 한번만 칼질, 4면, 2번칼질 = 3번 돌리면 됨. cuts = 0,1,2

for k in range(cuts):
    len = int(n / (2**k)) #한변의 길이가 처음엔 전체, 두번째엔 절반
    count = int(n/len)**2    # 한 변에 사각형의 갯수. 4에서 k=1일떄, 2x2 사각형 네개로 찢어짐


##yet solving