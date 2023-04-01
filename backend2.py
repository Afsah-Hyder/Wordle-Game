import enchant
from random import choice,choices


# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
# Function to check if it is safe to go to cell (x, y) from the current cell.
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed.
def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        and not processed[x][y]
 
 
# A recursive function to generate all possible words in a boggle
def searchBoggle(board, dictionary, result, processed, i, j, path=''):
    # mark the current node as processed
    processed[i][j] = True
 
    # update the path with the current character and insert it into the set
    path += board[i][j]
    
    if dictionary.check(str(path))==True and len(path)>=3:
        result.append(path)
    # check whether the path is present in the input set
    # if path in dictionary:
    #     result.add(path)
 
    # check for all eight possible movements from the current cell
    for k in range(len(row)):
        # skip if a cell is invalid, or it is already processed
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, dictionary, result, processed, i + row[k], j + col[k], path)
 
    # backtrack: mark the current node as unprocessed
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
 
    # construct a set to store valid words constructed from the boggle
    result = []
 
    # base case
    if not board or not len(board):
        return
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    # construct a boolean matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]
 
    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run DFS
            searchBoggle(board, words, result, processed, i, j)
 
    return result

def generate_board():
    uncommon=['c','j','q','v','w','x','y','z']
    common=['b','d','f','m','n','r','s','t','h','k','l','g','p']
    vowels=['a','e','i','o','u']
    board=[]
    num=3
    for i in range(num):
        board.append([])
    for i in range(num):
        for j in range(num):
            if i==1 and j==1:
                board[i].append(choice(vowels).upper())
            else:
                lst=[vowels,uncommon,common]
                x=choices(lst,weights=(0.25,0.2,0.55),k=1)
                letter=choice(x[0])
                board[i].append(letter.upper())
    return board

dictionary=enchant.Dict("en_US")

if __name__ == '__main__':
    board=generate_board()
    print(board)
    validWords = searchInBoggle(board, dictionary)
    print(validWords)