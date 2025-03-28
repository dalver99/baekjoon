from collections import deque
tries = deque()
N,K = map(int,input().split())
tries.append((K,0))
nums = set()

while tries:
    now,now_time = tries.popleft()
    if now < N:
        ()
        #print("too small")
    elif now_time > 100:
        ()
        #print("too long")
    elif now > 100000:
        ()
        #print("too big")
    elif now == N:
        nums.append(now_time)
    elif now%2 == 0:
        tries.append((now//2,now_time))
    else:
        tries.append((now+1,now_time+1))
        tries.append((now-1,now_time+1))

print(min(nums))