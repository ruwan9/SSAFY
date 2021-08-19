arr = [4, 4, 4, 3, 3]	

def solution(arr):
    i = 0
    ans = [arr[0]]

    while i < len(arr)-1:
        if arr[i+1] != arr[i]:  #  다음 idx랑 비교해서 다른게 나오면 다음 idx 추가
            ans.append(arr[i+1])
        i += 1
    return ans

print(solution(arr))

# 2
def solution(arr):
    answer = []

    for i in range(len(arr)) :
        if i == 0 :
            answer.append(arr[i])
        elif arr[i-1] != arr[i] :
            answer.append(arr[i])
    return answer

# 3
def solution3(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: 
            continue
        a.append(i)   
    return a

print(solution3(arr))

print(arr[:])
print(arr[-1:])