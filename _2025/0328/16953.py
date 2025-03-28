A,B = map(int,input().split())

success = False
count = 1
while True:
    count += 1
    if B%10 == 1: #뗄수있음 때
        B = (B-1)/10
    elif B%2 == 0: #나눌 수 있음 나눠
        B /= 2
    else: #다 아니면 망했어
        print(-1)
        break
    if A == B:
        print(count)
        break
    if A > B:
        print(-1)
        break