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
