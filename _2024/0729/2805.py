import sys

def cut_estimate(x):
    return sum([max(0, tree - x) for tree in trees])


N, M = map(int,sys.stdin.readline().rstrip().split())
trees = [int(v) for v in sys.stdin.readline().rstrip().split()]

maxi = max(trees)
mini = 0

while mini <= maxi: 
    mid = (mini+maxi) //2 
    wood = cut_estimate(mid)
    if wood >= M:
        mini = mid+1
    else:
        maxi = mid-1
print(maxi)
    