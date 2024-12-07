# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = [] 
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
        
        
    scores = list(set(scores))
    scores.sort()
    students.sort()
    del scores[0]
    
    
    for student in students:
        if student[1] == scores[0]:
            print(student[0])



""" 
# ==================================  Optimized ================================
if __name__ == '__main__':
    # Input number of students and their data
    students = [[input(), float(input())] for _ in range(int(input()))]

    # Extract scores and find the second lowest score
    scores = sorted(set(student[1] for student in students))
    second_lowest_score = scores[1]  # Get the second lowest score directly

    # Filter students with the second lowest score and sort them by name
    result = sorted(student[0] for student in students if student[1] == second_lowest_score)

    # Print the names of students with the second lowest score
    for name in result:
        print(name)
"""