N, r, c = map(int,input().split())

# 4진법으로 나타내야하고, 자릿수는 N자리수임. 맨 앞자리부터 하나씩 알아가는 방식임.
four = []
half = 2**N/2
for i in range(N):
    if r >= half and c >= half:
        four.append(3)
        r -= half
        c -= half
    elif r >= half and c <= half:
        four.append(2)
        r -= half
    elif r < half and c >= half:
        four.append(1)
        c -= half
    elif r < half and c <= half:
        four.append(0)

    half /= 2
#print(four)
ans = 0
for k in range (len(four)):
    ans += (4**k) * four[len(four)-k-1]
print (ans)