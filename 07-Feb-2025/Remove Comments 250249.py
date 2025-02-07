# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        block_comment= False
        new_line=[]
        for line in source:
            i = 0
            while i < len(line):
                if not block_comment:
                    if i + 1 < len(line) and line[i:i+2] == "//":
                        break
                    elif i + 1 < len(line) and line[i:i+2] == "/*":
                        block_comment = True
                        i +=1
                    else:
                        new_line.append(line[i])
                else:
                    if i+1 <len(line) and line[i:i+2]=="*/":
                        block_comment = False
                        i +=1
                i +=1
            if not block_comment and new_line: 
                result.append("".join(new_line))
                new_line = []
        return result


                

        