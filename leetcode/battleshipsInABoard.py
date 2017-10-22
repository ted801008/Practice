def countBattleships(board):
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                	print(i,j)
                	count+=1
        return count

board = [['.','.','.','X'],['X','X','X','X'],['.','.','.','X']]
print(countBattleships(board))