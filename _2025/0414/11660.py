#채워져있는 방식이.. 없음
#가로로 미리 다 누적합해둔다음
#세로로 2차로 누적합 해두면 될듯....?
import sys
N,M = map(int,input().split())

original_matrix = []
for _ in range(N):
    row = list(map(int,input().split()))
    original_matrix.append(row)
    