sik = input()
addthis = sik.split('-')
num = []
for eachones in addthis:
#    print(eachones)
    if '+' in eachones:
#        print('add found')
        eacheachones = eachones.split('+')
        temp = 0
        for nums in eacheachones:
            temp += int(nums)
        num.append(temp)
    else:
#        print('just num')
        num.append(int(eachones))

#print(num)
now = num.pop(0)
while len(num)>0:
    now -= num.pop(0)

print(now)
