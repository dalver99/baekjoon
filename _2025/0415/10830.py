#이거 무슨 분할정복 dp아닌가
#반토막내고 홀수면 한번 빼서 반토막내고.. 그런거아님?
N,B = map(int,input().split())


def mat_mul(A,B):
    for i in range (N):
        for j in range (N):