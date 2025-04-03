first = input()
second = input()
third = input()

N = -1

if first.isdigit():
    N = int(first) + 3
#    print('f')
if second.isdigit():
    N = int(second) + 2
#    print('s')
if third.isdigit():
    N = int(third) + 1
#    print('t')

if N%3 == 0 and N%5 == 0:
    print("FizzBuzz")
elif N%3 == 0:
    print("Fizz")
elif N%5 == 0:
    print("Buzz")
else:
    print(N)