n = int(input())
    

for _ in range(n):
    error = False
    order = list(input())
    arrnum = int(input())
    original = str(input().strip("[]"))
    numlist = original.split(',')

    if arrnum == 0:
        error = True
    else:
        for i in range(len(order)):
            if order[i] == 'R':
                #reverse
                numlist.reverse()
            else:
                if len(numlist) == 0:
                    error = True
                else:
                    numlist.pop(0)
                
    if not error:
        print('[',end='')    
        for numbers in numlist:
            if numlist.index(numbers) != len(numlist)-1:
                print(numbers,end=',')
            else:
                print(numbers,end='')
        print(']')
    else:
        print('error')