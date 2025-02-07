arr = [[2, 3], [1, 2], [0, 4], [2, 2]]

arr.sort(key=lambda x: (x[1], x[0]), reverse=True)

print(arr)