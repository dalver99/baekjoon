n = int(input())

sequence = [int(input()) for _ in range(n)]
print(sequence)

testlist = list()
for i in range (n):
    testlist.append(int(i)+1)

print(int(testlist.pop(0)))
