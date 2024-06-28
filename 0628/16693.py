import math
# slice
a1,p1 = map(int,input().split())
#whole
r1,p2 = map(int,input().split())

dpps = a1/p1 
dppw = (r1*r1*math.pi)/p2

if dpps > dppw:
    print('Slice of pizza')
else: 
    print('Whole pizza')

