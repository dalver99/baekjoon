N = int(input())

#1 1
#2-7 1+(1-6)
#8-19 1+6+(1-12)
#20-37 1+6+12+(1-18)

#1,7,19,37,61,..
#0,1,2-3,4-6,7-10

ssum = 1
temp = 1
while ssum < N:
    ssum += 6*temp
    temp += 1
    #print(ssum)

print(temp)