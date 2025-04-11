import sys
N = int(input())
array = []

for _ in range (N):
    array.append(int(input()))

#각 숫자에 대해서, 연속 5개가 되려면 몇개의 숫자가 부족한지를 셀 수 있는가
#없다면, 연속 5개가 되려면 필요한 숫자가 있는지 파악할 수 있는가 > 일단 이걸로
##다만 이렇게 하면 예를들어.. 3456 이라고 하면, 3에서랑 6에서 중복으로 세게 된다. 
###연속된 숫자만 확인해서 하면?3 5 7이런 케이스를 처리하기가 꽤 어려울 것 같음.


#일단 하나씩 확인해보자.
#모두 다른 숫자가 들어오기에, set로 하는 것이 빠름.
set_nums = set(array)

max_count = 0
for element in set_nums:
    #print(element)
    count = 1
    if element+1 in set_nums:
        count += 1
    if element+2 in set_nums:
        count += 1
    if element+3 in set_nums:
        count += 1
    if element+4 in set_nums:
        count += 1
    max_count = max(max_count,count)

print(5-max_count) # > OKAY. 맞았다. 36ms

#이러면 앞으로만 세기는 함. 3456일때, 3일때 7만 없으니까 1인거고. 2가 있었으면 됐을텐데 라는 가정은 없는 상황.
#사람은 연속된게 4개네? 하나 추가할까? 할텐데 .. 연속된 것을 판단하는 것 자체가 비효율적임으로 pass



#이딴 쓰레기같은 방법말고 머리를 써보자...


# sorted_array = sorted(array)
# max_count = 0
# if N == 1:
#     print(4)
#     sys.exit()
# if N == 2:
#     if sorted_array[0] +1 == sorted_array[1]:
#         print(3)
#     else:
#         print(4)
#     sys.exit()

# if N == 3:
#     for idx in range(0,N-3): # N-3~N-1까지 하면 3개니까 가능은함
#         now = sorted_array[idx]
#         count = 0
#         if sorted_array[idx+1] == now+1:
#             count += 1
#         if sorted_array[idx+2] == now+2:
#             count += 1
#         max_count = max(max_count,count)

# if N == 4:
#     for idx in range(0,N-4): # N-3~N-1까지 하면 3개니까 가능은함
#         now = sorted_array[idx]
#         count = 0
#         if sorted_array[idx+1] == now+1:
#             count += 1
#         if sorted_array[idx+2] == now+2:
#             count += 1
#         max_count = max(max_count,count)


# for idx in range(0,N-5): # N-5~N-1까지 하면 5개니까 가능은함
#     now = sorted_array[idx]
#     count = 0
#     if sorted_array[idx+1] == now+1:
#         count += 1
#     if sorted_array[idx+2] == now+2:
#         count += 1
#     if sorted_array[idx+3] == now+3:
#         count += 1
#     if sorted_array[idx+4] == now+4:
#         count += 1
#     max_count = max(max_count,count)

# print(5-max_count)