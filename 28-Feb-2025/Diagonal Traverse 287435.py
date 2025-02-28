# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows = len(mat)
        cols= len(mat[0])

        res=[]

        cur_row = cur_col = 0
        going_up = True

        while len(res) < rows * cols:
            res.append(mat[cur_row][cur_col])

            if going_up:
                if cur_col == cols -1:

                    cur_row +=1
                    #cur_col +=1
                    goind_up= False

                elif cur_col == 0:
                    cur_col +=1
                    going_up = False
                else:
                    cur_row -=1
                    cur_col +=1
            else :
                if cur_row == -1:
                    cur_col +=1
                    going_up =True

                elif cur_row == 0:
                    cur_row +=1
                    going_up = True
                else: 
                    cur_col -=1
                    cur_row +=1

        return res



                