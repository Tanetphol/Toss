board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
warningindex = [[],[]]
warning = []
count = 0

    
for i in range (len(board)):
    for j in range (len(board[0])):
        if "M" in board[i][j]:
            print('found bomb at :',i,j)#if bomb ar 12 warning should be 01 02 03 11 13 21 22 23 i range = 0-2 j range = 1-3
            for z in range (i-1,i+2):
                if z is not i and z>=0 and z<=len(board):
                    warningindex[0].append(z)
            for z2 in range (j-1,j+2):
                if z2 is not j and z2>=0 and z<=len(board[0]):
                    warningindex[1].append(z2)
            for i2 in range (warningindex[0][0],warningindex[0][1]+1):
                for i3 in range (warningindex[1][0],warningindex[1][1]+1):
                    warning.append([i2,i3])
                    if board[i2][i3] != board[i][j]:
                        board[i2][i3] = str(count)
                        print(board)
                        

if board[click[0]][click[1]] == "M":
    board[click[0]][click[1]] = "X"


            