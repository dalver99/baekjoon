#한번에 여러번 출연하는 경우만 세는 것도 가능

N = int(input())
M = int(input())
S = input()

i = 0
count = 0
result = 0

while i < M - 1:
    if S[i] == 'I' and S[i+1] == 'O': #시작
        temp_count = 0
        while i + 2 < M and S[i+1] == 'O' and S[i+2] == 'I': #길이 몇짜리니
            temp_count += 1
            i += 2
        if temp_count >= N:
            result += temp_count - N + 1
        else:
            i += 1
    else:
        i += 1

print(result)
