N = int(input())
q = [i for i in range (1,N+1)]
while len(q) > 1:
    #print(q)
    if len(q)%2 == 1: #홀수개인경우 7, 7+1 / 2개를 제거
        #for i in range (int((len(q)+1)/2)): #0,1,2,3
        for i in range((len(q) + 1) // 2 - 1, -1, -1):  # Reverse order
            q.pop(2*i)
        temp = q.pop(0)
        q.append(temp)
    else: #짝수개인경우 6, 3개를 제거
        #for i in range (int(len(q)/2)): #0,1,2 #정방향으로 하면 꼬임..
        for i in range(len(q) // 2 - 1, -1, -1):
            q.pop(2*i)
        
    # q.pop(0)
    # temp = q.pop(0)
    # q.append(temp)

print(*q)

# 123456 > 246
# 1234567 > (246) > 462