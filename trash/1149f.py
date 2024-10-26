N = int(input())

#경우의수가 6가지 뿐이다.
#그 여섯가지만 뽑아가면서 하자.

sixcase = [0,0,0,0,0,0]

#N이 2일 수 있다. 이때도 6가지다!

for i in range (N):
    three = list(map(int,input().split()))
    if i%3 == 0:
        sixcase[0] += three[0] #RGB
        sixcase[1] += three[0] #RBG
        sixcase[2] += three[1] #GRB
        sixcase[3] += three[1] #GBR
        sixcase[4] += three[2] #BRG
        sixcase[5] += three[2] #BGR
    elif i%3 ==1:
        sixcase[0] += three[1] #RGB
        sixcase[1] += three[2] #RBG
        sixcase[2] += three[0] #GRB
        sixcase[3] += three[2] #GBR
        sixcase[4] += three[0] #BRG
        sixcase[5] += three[1] #BGR
    else:  
        sixcase[0] += three[2] #RGB
        sixcase[1] += three[1] #RBG
        sixcase[2] += three[2] #GRB
        sixcase[3] += three[0] #GBR
        sixcase[4] += three[1] #BRG
        sixcase[5] += three[0] #BGR

print(min(sixcase))

#shit