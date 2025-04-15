def addstring(original,add):
    if original:
        return original + "\n" + add
    else:
        return add
        
t0="  *  "
t1=" * * "
t2="*****"

first = addstring("",t0)
first = addstring(first,t1)
first = addstring(first,t2)

a,b,c = first.split("\n")

second = ""
second = addstring(second," "*3*1 + a +" "*3*1)
second = addstring(second," "*3*1 + b +" "*3*1)
second = addstring(second," "*3*1 + c +" "*3*1)
second = addstring(second,a +" "+ a)
second = addstring(second,b +" "+ b)
second = addstring(second,c +" "+ c)


rows = second.split("\n")
third = ""
for idx,row in enumerate(rows):
    third = addstring(third," "*3*2 + row + " "*3*2)        
for idx,row in enumerate(rows):
    third = addstring(third,row + " " + row)
#12


rows = third.split("\n")
four = ""
for row in rows:
    four = addstring(four," "*3*(2**2) + row + " "*3*(2**2))        
for row in rows:
    four = addstring(four,row + " " + row)
#print(four)
#24

k = []
k.append(first)
k.append(second)
k.append(third)
k.append(four)

#k=4,5,6,7,8,9,10 까지만 하면 된다. 먼저 k=4, 총 48부터 하자.

for i in range (3,10):
    rows = k[-1].split("\n")
    temp = ""
    for row in rows:
        temp = addstring(temp," "*3*(2**i) + row + " "*3*(2**i))        
    for row in rows:
        temp = addstring(temp,row + " " + row)
    k.append(temp)

N = int(input())
print(k[N])
