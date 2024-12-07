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