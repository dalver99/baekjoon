import sys
import math

def isprime(find):
    if find == 1:
        return False

    for i in range (2,int(math.sqrt(find)+1)):
        if find%i == 0:
            return False
    return True

def main():
    n = int(sys.stdin.readline())
    user_input = sys.stdin.readline()
    numbers = list(map(int, user_input.split()))

    # print(numbers)
    count = 0
    i = 0
    for i in range(n):
        #if prime add 1
        count += int(isprime(numbers[i]))
        #print(int(isprime(numbers[i])))
        #if not prime pass

    sys.stdout.write(str(count))

if __name__ == '__main__':
    main()