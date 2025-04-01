# -54까지만 하면 되는 거 아님?

N = int(input())

oneofthese = []

for i in range (1,55):
    candidate = N - i
    summ = 0
    while candidate > 0:
        summ += candidate%10
        candidate = candidate//10
    if summ+N-i == N:
        oneofthese.append(N-i)

if oneofthese:
    print(min(oneofthese))
else:
    print(0)