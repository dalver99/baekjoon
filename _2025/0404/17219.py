import sys
input = sys.stdin.readline

N,M = map(int,input().split())

pw_dict = {}
#list는 tuple을 찾으려면 O(N)이 나와서 너무 오래걸림
#dict도 hashmap으로 찾는 속도는 O(1)임

for _ in range(N):
    site,pw = map(str,input().split())
    pw_dict[site] = pw

for _ in range(M):
    whatsite = input().strip()
    print(pw_dict[whatsite])
