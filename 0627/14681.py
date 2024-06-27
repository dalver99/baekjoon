import sys

def main ():
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    quad = 0

    if x > 0:
        if y > 0:
            quad = 1
        if y < 0:
            quad = 4
    if x < 0:
        if y > 0:
            quad = 2
        if y < 0:
            quad = 3

    sys.stdout.write(str(quad))


if __name__ == '__main__':
    main()