numbers = [2,1,3,4,1]	

def solution(numbers):
    new_num = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            new_num.append(numbers[i] + numbers[j])

    return sorted(list(set(new_num))) # set사용해서 중복 제거, sorted로 오름차순

# 2
from itertools import combinations

def solution2(numbers):
    answer = set()
    
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
        
    return sorted(answer)