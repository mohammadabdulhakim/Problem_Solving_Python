# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_scores = student_marks[input()]
    
    average = sum(query_scores) / len(query_scores)
    
    str_average_100 = str(int(average * 100))
    output = str_average_100[0:len(str_average_100)-2] + "." + str_average_100[len(str_average_100)-2:]
    
    print(output)
    
  
""" 
# ==================================  Optimized ================================
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))

    query_scores = student_marks[input()]
    average = sum(query_scores) / len(query_scores)

    # Format the average to 2 decimal places using f-string
    print(f"{average:.2f}")
"""