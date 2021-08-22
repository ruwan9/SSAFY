d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    answer = 0
    count = 0
    d.sort()

    for i in d :
        answer += i
        count += 1

        if answer > budget : 
            answer -= i
            count -= 1
            
    return count

print(solution(d, budget))