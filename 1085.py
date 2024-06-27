import sys

def main():
    fourint = sys.stdin.readline().split()
    x = int(fourint[0])
    y = int(fourint[1])
    w = int(fourint[2])
    h = int(fourint[3])

    shortesroute = min((x),((h-y)),(y),((w-x)))
    sys.stdout.write(str(shortesroute))


if __name__ == '__main__':
    main()