while True:
    threeint = list(map(int,input().split()))

    if threeint[0] == threeint[1] == threeint[2] == 0:
        break
    
    if threeint[0]**2 == (threeint[1]**2 + threeint[2]**2):
        print('right')
    elif threeint[2]**2 == (threeint[1]**2 + threeint[0]**2):
        print('right')
    elif threeint[1]**2 == (threeint[0]**2 + threeint[2]**2):
        print('right')
    else:
        print('wrong')
