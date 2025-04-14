#채워져있는 방식이.. 없음
#가로로 미리 다 누적합해둔다음
#세로로 2차로 누적합 해두면 될듯....?
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

# original_matrix = []
# for _ in range(N):
#     row = list(map(int,input().split()))
#     original_matrix.append(row)

original_matrix = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = (
            prefix_sum[i-1][j] +
            prefix_sum[i][j-1] -
            prefix_sum[i-1][j-1] +
            original_matrix[i-1][j-1]
        )



# side_add_matrix = []
# for i in range(N):
#     row = original_matrix[i]
#     new_row = [row[0]]
#     for j in range(1,N): 
#         # row[j+1] = row[j]+row[j+1]
#         new_row.append(new_row[-1]+row[j])
#     side_add_matrix.append(new_row)

# #print(side_add_matrix)

# column_add_matrix = []
# column_add_matrix.append(side_add_matrix[0])
# for i in range(N-1):
#     row = [x+y for x,y in zip(side_add_matrix[i+1],column_add_matrix[-1])]
#     column_add_matrix.append(row)

# #print(column_add_matrix)

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        ans = prefix_sum[y2-1][x2-1]
    elif x1 == 1:
        ans = prefix_sum[y2-1][x2-1] - prefix_sum[y1-2][x2-1]
    elif y1 == 1:
        ans = prefix_sum[y2-1][x2-1] - prefix_sum[y2-1][x1-2]
    else:
        ans = prefix_sum[y2-1][x2-1] - prefix_sum[y2-1][x1-2] - prefix_sum[y1-2][x2-1] + prefix_sum[x1-2][y1-2]

    print(ans)

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1  # 인덱스 조정

#     total = column_add_matrix[x2][y2]
#     if x1 > 0:
#         total -= column_add_matrix[x1-1][y2]
#     if y1 > 0:
#         total -= column_add_matrix[x2][y1-1]
#     if x1 > 0 and y1 > 0:
#         total += column_add_matrix[x1-1][y1-1]
#     print(total)

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = (
#         prefix_sum[x2][y2]
#         - prefix_sum[x1-1][y2]
#         - prefix_sum[x2][y1-1]
#         + prefix_sum[x1-1][y1-1]
#     )
#     print(result)

#코테 전에 다시 해보자
