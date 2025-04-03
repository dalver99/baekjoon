import sys
input = sys.stdin.readline
N = int(input())
users = [] 

for _ in range (N):
    age,user = map(str,input().split())
    users.append([int(age),user])

sorted_users = sorted(users,key=lambda x: (x[0]))

for each_user in sorted_users:
    print(*each_user)