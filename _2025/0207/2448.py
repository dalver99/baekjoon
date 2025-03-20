N = int(input())

#총 가로길이는 5, 11, 23, ..
garo = N*2-1

#세줄짜리 행렬을 받아서, 삼각형을 append하고 리턴하는 함수
def add_triangle(row1,row2,row3):
    row1 = row1 + ("  *  ")
    row2 = row2 + (" * * ")
    row3 = row3 + ("*****")
    return(row1,row2,row3)

#세줄짜리 행렬을 받아서, 앞에 빈칸을 추가하는 함수
def add_space(row1,row2,row3,space):
    row1 = " "*space + row1
    row2 = " "*space + row2
    row3 = " "*space + row3
    return(row1,row2,row3) 

matrix = [[] for _ in range (N)]
print(matrix)

for j in range(1):
    matrix[0],matrix[1],matrix[2] = add_triangle("","","")

for k in range(len(matrix)):
    print(matrix[k])