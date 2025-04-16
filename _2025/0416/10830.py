#이거 무슨 분할정복 dp아닌가
#반토막내고 홀수면 한번 빼서 반토막내고.. 그런거아님?
import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

N,B = map(int,input().split())

def mat_mul(A,B):
    C = [[0]*N for _ in range(N)]
    # 1 2 3    1 1 1   1*1 2*2 3*3  
    # 4 5 6    2 2 2   4*1 5*2 6*3
    # 7 8 9    3 3 3
    for i in range (N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= 1000
    return C

mat_A = []

for _ in range (N):
    row = list(map(int,input().split()))
    mat_A.append(row)

@lru_cache(maxsize=None)
def mat_pow(power):
    if power == 1:
        return [[elem % 1000 for elem in row] for row in mat_A]
    now = power // 2
    ans = mat_A
    if power %2 == 0:
        ans = mat_mul(mat_pow(now),mat_pow(now))
    else:
        ans = mat_mul(mat_mul(mat_pow(now),mat_pow(now)),mat_A)
    return ans

mat = mat_pow(B)
for row in mat:
    print(*row)
