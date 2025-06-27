# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isvalid(row,col,board):
            for i in range(row):
                if board[i]==col or (abs(row-i)==abs(col-board[i])):
                    return False
            return True
        res=[]
        board=[-1]*n
        def backtrack(n,k,board):
            if k==n:
                call(board)
                return
            for i in range(n):
                if isvalid(k,i,board):
                    board[k]=i
                    backtrack(n,k+1,board)
        def call(board):
            l=[]
            for i in range(n):
                ans=''
                for j in range(n):
                    if board[i]==j:
                        ans+='Q'
                    else:
                        ans+='.'
                l.append(ans)
            res.append(l)
        backtrack(n,0,board)
        return res
        