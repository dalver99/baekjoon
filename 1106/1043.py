import sys
input = sys.stdin.readline

N,M = map(int,input().split())
second_input = list(map(int,input().split()))

those_who_know_the_truth = []
if second_input[0] != 0:
    second_input.pop(0)
    those_who_know_the_truth = second_input

party_people = []
for i in range(M):
    each_party = list(map(int,input().split()))
    each_party.pop(0)
    party_people.append(each_party)

#print(party_people)
flag = True
while flag:
    flag = True
    for idx, party in enumerate(party_people):
        if any(those_who_know_the_truth) in party:
            #이걸 언제까지 반복해야함? - 단 한번도 진실을 아는사람이 파티에 참여하지 않을때까지!!
            flag = False
            #그 파티에 나머지 사람들도 다 truth list에 추가하고
            for person in party:
                print("ITERATING",person)
                if person not in those_who_know_the_truth:
                    those_who_know_the_truth.append(person)
                    print("UPDATED WHO KNOW THE TRUTH",those_who_know_the_truth)
                    flag = True
            #그 파티를 삭제해야됨
            party_people.pop(idx)
            print("UPDATED PARTY", party_people)
    
print(party_people)
print(len(party_people))