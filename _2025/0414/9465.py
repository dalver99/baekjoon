import sys
input = sys.stdin.readline

T = int(input())

for _ in range (T):
    N = int(input())
    stickers = []
    stickers.append(list(map(int,input().split())))
    stickers.append(list(map(int,input().split())))

    # print(stickers)
    # DP 계획은.. N번쨰 열의 0번행, 1번행을 고른 두가지 경우에서 최대가 되는 케이스를 가지고 있자. 맨 끝까지 가서, 0행과 1번행 중 더 큰 숫자를 고르면 그게 최대치임
    #각, 하나 전에서 대각선으로 고르거나, 두개 전에서 반대행을 고르는 경우만 비교해서 갖고 있짜.
    

    #N은 1~100,000. 1/2는 예외처리가 필요함.
    if N == 1:
        print(max(stickers[0][0],stickers[1][0]))
        continue
    if N == 2:
        print(max(stickers[0][0]+stickers[1][1],stickers[1][0]+stickers[0][1]))
        continue

    DP = [[0]*N for _ in range(2)] #[0][N] [1][N]
    DP[0][0] = stickers[0][0]
    DP[1][0] = stickers[1][0]

    DP[0][1] = stickers[0][1] + stickers[1][0]
    DP[1][1] = stickers[1][1] + stickers[0][0]

    for i in range (0,N-2):
        DP[0][i+2] = max(DP[1][i+1]+stickers[0][i+2],DP[1][i]+stickers[0][i+2])
        DP[1][i+2] = max(DP[0][i+1]+stickers[1][i+2],DP[0][i]+stickers[1][i+2])

    print(max(DP[0][N-1],DP[1][N-1]))