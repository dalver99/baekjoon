def chinese_remainder_theorem(m, n, x, y):
    while(x <= m*n):
        if(x%n == y%n):
            return x
        x += m
    return -1

t = int(input().strip())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(chinese_remainder_theorem(m, n, x, y))