#아름답게 풀고 싶지만
#가장 큰 테트리미노가 가장 큰 두개의 합도, 가장큰 숫자도 포함한다는 것은 거짓된 가정임
#ex
# 9 8 0 0
# 0 0 2 4
# 0 0 6 7
# 0 0 0 0
N,M = map(int,input().split())
graph = []
for _ in range (N):
    row = list(map(int,input().split()))
    graph.append(row)

#그냥 다 해보자
#모두 왼쪽 위에서부터 오른쪽 아래로 훑어나간다고 가정하자.
#제일 왼쪽 위 사각형을 가지고 시작하자. 
#일자
shape11 = [[1,0],[2,0],[3,0]] # ㅡ
shape12 = [[0,1],[0,2],[0,3]] # ㅣ
#사각형
shape21 = [[1,1],[1,0],[0,1]] # ㅁ
#주황색L
shape31 = [[0,-1],[0,-2],[1,0]] #L #17말고 18
shape32 = [[1,0],[2,0],[2,-1]] #__|
shape33 = [[1,0],[1,1],[1,2]] #90도 반시계로 더 ㄱ
shape34 = [[0,-1],[1,-1],[2,-1]] #.--
#파란색L
shape41 = [[1,-1],[1,-2],[1,0]] #_|
shape42 = [[0,-1],[1,-1],[2,-1]] #|__
shape43 = [[0,1],[0,2],[1,2]] #ㅡㅡ|
shape44 = [[0,-1],[0,-2],[1,-2]] #|ㅡ
#초록색ㄹ
shape51 = [[0,1],[1,1],[1,2]] #백준4번그림
shape52 = [[1,0],[1,-1],[2,-1]] #백준4번그림 시계방향 90도 _-
#빨간색ㄹ
shape61 = [[0,-1],[1,-1],[1,-2]]#백준 4번그림 좌우대칭, 왼쪽아래부터
shape62 = [[1,0],[1,1],[2,1]] #를 90도 -_
#뻐큐
shape71 = [[1,0],[1,1],[2,0]] # ㅗ
shape72 = [[1,0],[1,-1],[2,0]] # ㅜ
shape73 = [[1,0],[1,1],[1,-1]] # ㅓ
shape74 = [[1,0],[0,1],[0,-1]] # ㅏ

shapes = []
shapes.append(shape11)
shapes.append(shape12)
shapes.append(shape21)
shapes.append(shape31)
shapes.append(shape32)
shapes.append(shape33)
shapes.append(shape34)
shapes.append(shape41)
shapes.append(shape42)
shapes.append(shape43)
shapes.append(shape44)
shapes.append(shape51)
shapes.append(shape52)
shapes.append(shape61)
shapes.append(shape62)
shapes.append(shape71)
shapes.append(shape72)
shapes.append(shape73)
shapes.append(shape74)

shapes2 = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]


def pointcalc(y,x):
    global ans
    for i in range(len(shapes2)):
        result = graph[y][x]
        # print("###")
        # print(x,y)
        for j in range(3):
            try:
                nx = x + shapes2[i][j][0]
                ny = y + shapes2[i][j][1]
                result += graph[ny][nx]
            except IndexError:
                result = 1
                break
        # print(result)
        # print("###")

        ans = max(ans,result)

ans = 0
for ii in range(N):
    for jj in range(M):
        pointcalc(ii,jj)

print(ans)