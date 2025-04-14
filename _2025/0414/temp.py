a = [0,0,0,1]
b = [1,0,0,0]

print(a+b)

result = [x+y for x,y in zip(a,b)]
print(result)