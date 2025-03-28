import math
def is_prime(N):
    ip = True
    if N == 1:
        return False
    
    for i in range (2,int(math.sqrt(N))+1):
        if N%i == 0:
            return False
        
    return ip
            
M,N = map(int,input().split())
for nums in range(M,N+1):
    if is_prime(nums):
        print(nums)


# M,N = map(int,input().split())
# nums = []
# for i in range (M,N+1):
#     nums.append(i)
    