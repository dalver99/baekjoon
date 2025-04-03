input()
hashthis = input()

#print(ord('a')-96) #this is where we start

sum = 0
for i,letter in enumerate(hashthis):
    ai = ord(letter) - 96
    sum += ai * (31 ** i)

print(sum%1234567891)
