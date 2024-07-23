string = list(str(input()))
n = len(string)
for idx in range(26):
    try: 
        print(string.index(chr(ord('a')+idx)))
    except:
        print('-1')
