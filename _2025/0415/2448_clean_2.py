def addstring(original, add):
    return original + "\n" + add if original else add

t = ["  *  ", " * * ", "*****"]
first = addstring("",t[0])
first = addstring(first,t[1])
first = addstring(first,t[2])

k = [first]

for i in range (0,10):
    rows = k[-1].split("\n")
    temp = ""
    for row in rows:
        temp = addstring(temp," "*3*(2**i) + row + " "*3*(2**i))        
    for row in rows:
        temp = addstring(temp,row + " " + row)
    k.append(temp)

N = int(input())
print(k[N])