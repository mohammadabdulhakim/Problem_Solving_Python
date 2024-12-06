# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

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
    

""" 
# ==================================  Optimized ================================
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    
    # Remove duplicates by converting to a set
    unique_scores = set(scores)
    
    # Find the maximum score
    max_score = max(unique_scores)
    
    # Remove the maximum score to find the runner-up
    unique_scores.remove(max_score)
    
    # The runner-up score is the next maximum
    runner_up_score = max(unique_scores)
    
    print(runner_up_score)
"""