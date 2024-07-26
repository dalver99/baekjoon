listt = []
for _ in range(9):
    listt.append(int(input()))

print(max(listt))
print(listt.index(max(listt))+1)
