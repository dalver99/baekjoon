
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
# first = first.strip("\n")

# print(first.lstrip("\n"))
# print(first.rstrip("\n"))

#print(first.split("\n"))
#first를 to,t1,t2로 분해해보자.
a,b,c = first.split("\n")

second = ""
second = addstring(second," "*3*1 + a +" "*3*1)
second = addstring(second," "*3*1 + b +" "*3*1)
second = addstring(second," "*3*1 + c +" "*3*1)
second = addstring(second,a +" "+ a)
second = addstring(second,b +" "+ b)
second = addstring(second,c +" "+ c)

# second = second.strip("\n")
#print(second)

rows = second.split("\n")
third = ""
for idx,row in enumerate(rows):
    third = addstring(third," "*3*2 + row + " "*3*2)        
for idx,row in enumerate(rows):
    third = addstring(third,row + " " + row)

# third = third.strip("\n")
#12

rows = third.split("\n")
four = ""

for row in rows:
    four = addstring(four," "*3*(2**2) + row + " "*3*(2**2))        
for row in rows:
    four = addstring(four,row + " " + row)

# four = four.strip("\n")
print(four)
#24

k = []
k.append(first)
k.append(second)
k.append(third)
k.append(four)

print(k)