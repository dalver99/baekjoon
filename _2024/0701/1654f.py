k,n = map(int,input().split())

numbers = list()
for _ in range (k):
    a = int(input())
    numbers.append(a)

minimum = max(numbers)

for i in range(minimum):
    count = 0
    trydis = int(minimum)-int(i)
    for number in numbers:
        count += int(number/trydis)
    
    if count >= n:
        #print("okay! i is" + str(i) + ', count is' + str(count))
        ans = trydis
        break

if i == 0:
    #역방향으로 가야됨..
    for k in range(9999):
        count = 0
        trydis += k
        for number in numbers:
            count += int(number/trydis)#

        if count < n:
            ans = trydis +1
            break

print(ans)
#좀 더 알고리즘을 짜보자..