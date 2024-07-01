n,m = map(int,input().split())
counts = list()
count = 0
board = list()
for i in range (n):
    inp = input()
    board.append(inp)

#splitter
for h in range(n-7):
    longbox = board[h:h+8] # cut out A * 8 box
    for w in range (m-7): # iterate each box
        for wi in range (8): # iterate through each row
            row = longbox[wi][w:w+8] # cut out 8 from A
            for w8 in range(8):
            # core algorithm
                if (w8%2 + wi%2)%2 == 0:
                    # if row[w] == 'W':
                        # you're good
                    if row[w8] == 'B':
                        count += 1
                if (w8%2 + wi%2)%2 == 1:
                    if row[w8] == 'W':
                        count += 1
                    #if row[w] == 'B':
                        # you're good
        if count >= 33:
            count = 64-count
        counts.append(count)
        count = 0
        #print('###')

print(int(min(counts)))