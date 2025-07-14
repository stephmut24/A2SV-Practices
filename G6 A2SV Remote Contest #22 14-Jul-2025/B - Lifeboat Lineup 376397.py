# Problem: B - Lifeboat Lineup - https://codeforces.com/gym/622136/problem/B



def lifeboat_lineup(n, crew_lst):
    
    rats =[]
    women_children =[]
    men = []
    cap=""
    
    
    for name, status in crew_lst:
        if status == "rat":
            rats.append(name)
        elif status == "woman" or status =="child":
            women_children.append(name)
            
        elif status =='man':
            men.append(name)
            
        elif status == "captain":
            cap = name
            
    evacuation_order = rats + women_children +men + [cap]
    
    return evacuation_order


n =int(input())
crew_lst = [tuple(input().split()) for _ in range(n)]

order = lifeboat_lineup(n, crew_lst)

for name in order:
    print(name)
   


