# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scores = sorted(set([score for _, score in students]))
    
    if len(scores) < 2:
        exit()
    
    second_lowest_score = scores[1]
    
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    
    for student in sorted(second_lowest_students):
        print(student)