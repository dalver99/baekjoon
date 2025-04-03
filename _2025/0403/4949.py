text = "letsgo"

while True:
    text = input()
    if text == ".":
        break
    q = []

    for letter in text:
        if letter == '[' or letter == ']' or letter == '(' or letter == ')':
            q.append(letter)
        
    stringify = "".join(q)
    while True:
        if '()' in stringify or '[]' in stringify:
            stringify = stringify.replace("()","")
            stringify = stringify.replace("[]","")
        else:
            break
    if stringify == "":
        print('yes')
    else:
        print('no')