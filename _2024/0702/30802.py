n = int(input())

sizenums = list(map(int,(input().split())))
t,p = input().split()

tcount = 0

for number in sizenums:
    if number%int(t) != 0:
        tcount += (number//int(t)) + 1
    else:
        tcount += (number//int(t))

pencount = n%int(p)
pendiv = n//int(p)

print(tcount)
print(str(pendiv) +' '+str( pencount))


