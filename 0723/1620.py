import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())

pokemons_by_name = {}
pokemons_by_index = {}

# 각각 따로저장
for i in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    pokemons_by_name[name] = i
    pokemons_by_index[i] = name

for _ in range(Q):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():
        print(pokemons_by_index[int(quiz)])
    else:
        print(pokemons_by_name[quiz])
