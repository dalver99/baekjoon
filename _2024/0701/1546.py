n = int(input())
scores = list(map(int,(input().split())))
m = max(scores)
calav = 0
for score in scores:
    calav += (int(score)*100)/int(m)
    #print(calav)
print(int(calav)/n)