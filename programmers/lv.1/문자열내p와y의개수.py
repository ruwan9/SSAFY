s = "absc"
def solution(s):
    new_s = s.lower()
    if new_s.count('p') == new_s.count('y'):
        return True
    return False
print(solution(s))

#2
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution2(s))