import sys
from itertools import permutations

input = sys.stdin.readline

#N= int(input())

for N in range (1,15):
#일단 0~7이 든 배열 하나를 만들고
    basic = [i for i in range(N)]
    #print(basic)
    ans = 0
    #그걸 전부 다 경우의수를 만들고, 하나씩 돌려보면서 대각선이 합당한 지 확인
    for case in permutations(basic,r=N):
        thiscase = True
    #print(comb)
        #대각선은 아래로만 확인
        for j in range(N): #긱 행마다 .. 
            # case[j]가 현재 행에서 퀸이 있는 위치. 편의상 0,0을 체스판의 백색보드 a8이라 가정하자.
            #0번행은 7번 확인해야함, 7번행은 0번확인함
            for k in range(1,N-j): #아래로 내려가자.. 0행인경우 1행부터 7행까지 확인 1행인경우 2행부터 7행, ... 6행인경우 7행만 확인. 확인 횟수는 각 0행인 경우 7번, 6행인경우 1번

                #내려가서는, 좌우로 튀어나갔는지 확인하고 각각에 따라 .. 
                #우로 나갔는지 확인
                if case[j]+k < N:
                    #안 나갔다면, k칸을 내려가서, k만큼 더한것과 수치비교. 같으면 한 대각선상에 있는 것
                    if case[j]+k == case[j+k]:
                        thiscase = False
                        break

                #내려가서는, 좌우로 튀어나갔는지 확인하고 각각에 따라 .. 
                #좌로 나갔는지 확인
                if case[j]-k >= 0:
                    #안 나갔다면, k칸을 내려가서, k만큼 더한것과 수치비교. 같으면 한 대각선상에 있는 것
                    if case[j]-k == case[j+k]:
                        thiscase = False
                        break

            #어차피 안되는거면 그만확인
            if not thiscase:
                break
        #모든 행에 대해 성공적이었다면 성공
        if thiscase:
            ans += 1
            #print(case)

    print(ans)