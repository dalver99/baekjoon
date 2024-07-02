from operator import itemgetter

n = int(input())
a = list()
for i in range(n):
    x,y = map(int,input().split())
    a.append([])
    a[i].append(x)
    a[i].append(y)

a = sorted(a, key=itemgetter(1, 0)) #Sort by 'x' and then 'y'
for m,n in a:
    print(m,n)
    
