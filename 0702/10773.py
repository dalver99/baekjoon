n = int(input())
b = list()
for _ in range(n):
    inp = int(input())
    if inp != 0:
        b.append(inp)
    if inp == 0:
        b.pop()
print(sum(b))

