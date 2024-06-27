import sys
import math

def main():
    fourint = sys.stdin.readline().split()
    x = int(fourint[0])
    y = int(fourint[1])
    d = int(fourint[2])
    t = int(fourint[3])

    distance = math.sqrt(x**2 + y**2)
    dcopy = distance
    dcopy2 = distance
    walk = 0
    njump = 0
    jumppwalk =0
    # 걷는 경우는 점프를 안쓸때 뿐
    walk = distance

    # 점프 case1 = 점프가 어느정도커서 각잡아서 n번 뛰면 됨
    while dcopy >= d:
        njump += t
        dcopy -= d
    # 거리가 남거나 넘어간 경우, 점프 1회 추가
    if dcopy != 0:
        njump += t
    # 한번만에 뛴걸로 판단한 경우 검증
    if t == njump:
        if d != njump:
            njump += t

    # 점프 case2 = 남는거리 걸어서 처리해보기
    while dcopy2 >= d/2:
        jumppwalk += t
        dcopy2 -= d
    # 남은 거리는 걸어
    if dcopy != 0:
        jumppwalk += abs(dcopy2)

    # print('걸어서' + str(walk))
    # print('뛰기만' + str(njump))
    # print('섞어서' + str(jumppwalk))

    time = min(walk,njump,jumppwalk)
    sys.stdout.write(str(time))


if __name__ == '__main__':
    main()