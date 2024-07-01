n = int(input())
words = list()
for i in range (n):
    word = input()
    words.append(word)

words = list(set(words))
words.sort(key=lambda word : (len(word),word))

for x in words:
    print(x)