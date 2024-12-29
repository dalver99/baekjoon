n = int(input())

list = [int(v) for v in input().split()]
list.sort()
sum = 0
for i in range(len(list)):
    sum += list[(n-1)-i] * (i+1)

print(sum)