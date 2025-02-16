# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

x1, y1 = target

dist = abs(x1) +abs(y2)

for x2 , y2 in ghosts:
    if abs(x2-x1)+ abs(y2-y1) <= dist:
        return False
return True