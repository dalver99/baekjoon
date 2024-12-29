i = int(input())

for _ in range (i):
    oxlist = list(input())
    score = 0
    add = 0
    for j in range (len(oxlist)):
        if oxlist[j] == 'O':
            add += 1
            score += add
        if oxlist[j] == 'X':
            add = 0
    print(score)