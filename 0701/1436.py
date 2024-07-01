devil = list()
for i in range (2666999):
    if "666" in str(i):
        devil.append(i)
    if len(devil) == 10005:
        break
n = int(input())
print(devil[n-1])