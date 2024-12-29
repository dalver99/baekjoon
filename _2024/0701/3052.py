num = 0
b = list()
for i in range (10):
    a = int(input())
    c = a%42
    if c not in b:# is not in list b
        num += 1
        b.append(c)
        # insert a in list b

print(num)