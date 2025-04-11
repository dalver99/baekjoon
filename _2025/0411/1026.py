N = int(input())
one = sorted(list(map(int,input().split())))
two = sorted(list(map(int,input().split())),reverse=True)

sum = 0
for i in range (N):
    sum += one[i] * two[i] #머릿속으로 많이 따져봤는데 이정도면 될듯

print(sum)