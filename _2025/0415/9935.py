word = input()
bomb = input()
l = len(bomb)

# while True:
#     if bomb in word:
#         idx = word.index(bomb)
#         list_word = list(word)
#         for _ in range (l):
#             list_word.pop(idx)
#         word = "".join(list_word)
#     else:
#         print(word)
#         break
        
#이게 안되는 건 나도 아는데 해보고 싶었음
        
#인덱스 관리를 하면서 풀어야 할 듯함.

#좌에서 우로 훑으면서 폭발 문자열을 다 지우고,
#그걸 반복하는 방법은? 

# while True:
#     if word == "":
#         print("FRULA")
#     if bomb in word:
#         word = word.replace(bomb,'')
#     else:
#         print(word)
#         break

#44% 시간초과.

#스택에 한글자씩 넣다가, 방금 한글자를 넣었더니 패턴이 맨 뒤에 잡혔어 인 경우에 반복적으로 POP

stack = []
for each_letter in word:
    stack.append(each_letter)
    # print(stack[-l:])
    if len(stack) >= l and "".join(stack[-l:]) == bomb:
        for _ in range (l):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")

    #Nice!
    