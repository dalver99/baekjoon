N = int(input())

meetings = []

for _ in range (N):
    start,end = map(int,input().split())
    meetings.append((start,end))

meetings.sort(key = lambda x:(x[1],x[0]))

end = 0
number = 0

for meeting in meetings:
    if meeting[0] >= end:
        number += 1
        end = meeting[1]

print(number)
