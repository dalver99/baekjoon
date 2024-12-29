k,n = map(int,input().split())

numbers = list()
for _ in range (k):
    a = int(input())
    numbers.append(a)

sum = 0
for number in numbers:
    sum += int(number)

av = int(sum / n)
#print(av)

countk = 0
for number in numbers:
    countk += int(number/av)
    # test it!

if countk >= n:
    #number is too good, go up until fail
    for i in range (9999):
        countk = 0
        ans = av + i
        for number in numbers:
            countk += int(number/ans)
        if countk < n:
            ans -= 1
            break
if countk < n:
    #number is too high, go down until success
    for i in range (9999):
        countk =0
        ans = av - i
        for number in numbers:
            countk += int(number/ans)
        if countk >= n:
            break

print(ans)