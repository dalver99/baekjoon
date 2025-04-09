from collections import defaultdict
#코테.. 다시 해볼것

n = int(input())
fruit = list(map(int,input().split()))
start,end = 0,0
count = defaultdict(int)
max_count = 0

while end < n:
    count[fruit[end]] += 1 #그 과일의 개수에 하나 추가

    while len(count.keys()) > 2: #세다가 dict의 키값의 종류가 2가 넘어가면
        count[fruit[start]] -= 1 #처음에서 하나를 뺴봐 일단
        if count[fruit[start]] == 0: #그과일이 더이상 없으면
            del count[fruit[start]] #딕트에서 키 제거
        start += 1 #포인터 한칸 이동
    end += 1
    max_count = max(max_count,sum(count.values()))
print(max_count)