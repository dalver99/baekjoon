fivenum = list(input().split())
sum = 0

for i in range(len(fivenum)):
    sum += int(fivenum[i])**2

print(sum%10)
