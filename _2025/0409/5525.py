N = int(input())
M = int(input())
S = input()

temp = "I"*(N+1)
find = "O".join(list(temp))
# print(find)

def find_overlapppp(string,find):
    howmany = 0
    start = 0
    while start <= len(string) - len(find): #끝까지가면 더 안찾아도대
        if string[start:start+len(find)] == find:
            howmany += 1
        start += 1
    print(howmany)

find_overlapppp(S,find)