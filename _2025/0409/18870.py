N = int(input())
xis = list(map(int,input().split()))

#보다 작은 건 다 출력하는것임

xi_sorted = sorted(list(set(xis)))

dic = {xi_sorted[i]: i for i in range(len(xi_sorted))}

for i in xis:
    print(dic[i],end=' ') #오름차순으로 나열하면, 그 번호가 곧 나보다 작은 놈들의 갯수가 된다!!