first = input()
second = input()

LCS = 0
for each_letter in first: #그 수열이 어디서 시작할 진 모르는 거 아님? 모든 글자가 시작이라고 가정해보자.
    temp_LCS = 0
    temp_string = []
    temp_second = second
    #남은 글자수가 LCS보다 작으면 안될 거 아녀.
    if LCS > len(first) - first.index(each_letter):
        break
    
    idx = 0
    # searchidx = 0
    findthisletter = first[idx]

    while len(second):
        if findthisletter in second:
            # if second.index(findthisletter) >= searchidx:
                temp_string.append(findthisletter)
                temp_LCS += 1
                serachidx = second.index(findthisletter)
                #print(findthisletter)
        idx += 1
        if idx < len(first):
            findthisletter = first[idx]
        else:
            break
    print(temp_string)
    LCS = max(temp_LCS,LCS)

print(LCS)