t = int(input())
dynamic = [1,2,4,7]

for k in range(6):
    dynamic.append(dynamic[k+3] + dynamic[k+2] + dynamic[k+1])

for _ in range (t):
    n = int(input())
    print(dynamic[n-1])