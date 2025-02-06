# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(String):

    KevinPt=0
    StuartPt=0
    Vowel= "AEIOU"

    for i in range (len(String)):
        if String[i] in Vowel:
            KevinPt += len(String)-i
        else:
            StuartPt +=len(String)-i

    if StuartPt > KevinPt:
        print("Stuart", StuartPt )
    elif KevinPt > StuartPt:
        print("Kevin", KevinPt)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)