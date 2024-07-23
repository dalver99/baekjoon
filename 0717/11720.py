n = int(input())
string = list(str(input()))
sum = 0

for k in range(n):
    sum += int(string.pop(0))

print(sum)