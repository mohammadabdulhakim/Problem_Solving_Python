if __name__ == '__main__':
    n = int(input())
    input_arr = map(int, input().split())
    scores = list(input_arr)
    
    max_score = max(scores)
    second_score = min(scores)
    
    for score in scores:
        if score < max_score and score > second_score:
            second_score = score
    
    print(second_score)
    