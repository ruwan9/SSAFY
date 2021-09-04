participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	

# 1. 효율성 테스트 탈락
for i in completion:
    if i in participant:
        participant.remove(i)

# print(participant[0])


participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	

# 2. # zip() 이용
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]

"""
zip() : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수

ex) 
list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]

"""


# 3. hash() 이용
def solution2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution2(participant, completion))

"""
hash() : return the hash value of the object (if it has one)
-> 실행될 때마다 각 값에 대한 고유한 정수형 숫자 값을 반환

1. participant의 hash값들을 모두 더해주고
2. conpletion의 hash값들을 모두 더해줘서 
3. 두 값의 차를 구하면 participant 중 completion에 들어가지 못한 hash값 하나가 남게 된다.
"""