T = int(input())
ans = []

ans.append([i for i in range (1,15)])

for k in range (0,14):
    temp = []
    for i in range (1,15):
        summ = 0
        for j in range(i):
            summ += int(ans[k][j])
        temp.append(summ)
    ans.append(temp)
     
#print(ans)
#print(temp)

for _ in range(T):
    K = int(input())
    N = int(input())
    print(ans[K][N-1])

#ex k=1 n=3
#0층: 1,2,3
#1층: 1,3,6

#ex k=2, n=3
#0층: 1,2,3
#1층: 1,3,6
#2층: 1,4,10

#bigger ex
# 1 2 3 4 5
# 1 3 6 10 15
# 1 4 10 20 35