a = [0]
a.append(1)
a.append(2)
for i in range (999):
    a.append(a[i+1]+a[i+2])

n = int(input())
print(a[n]%10007)