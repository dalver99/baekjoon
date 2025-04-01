import sys,math 

input = sys.stdin.readline

N = int(input())

if N==0:
    print(0)
    sys.exit()

leesootoo = []
for _ in range(N):
    leesootoo.append(int(input()))

sorted_list = sorted(leesootoo, key = lambda x: x)
#print(sorted_list)

remove_howmany = math.floor(N*0.15+0.5)
#0,1,2,3 제외하고 4~20 까지 해야함 4~24-4
#print(remove_howmany)
front = sum(sorted_list[x] for x in range (0,remove_howmany))
#print(front)
back = sum(sorted_list[x] for x in range (N-remove_howmany,N))
#print(back)
this = (sum(sorted_list)-front-back)/(N-remove_howmany*2)
rounded = math.floor(this+0.5)
print(rounded)