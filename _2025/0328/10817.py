N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for i in range(len(A)):
    if A[i] < X:
        result.append(str(A[i]))  #마지막인지 구분이 불가능한 상황이라..

print(" ".join(result))