s = "Zbcdefg"
def solution(s):
    return ''.join(sorted(s, reverse = True))  # sorted() 사용하면 리스트 반환, ''.join()으로 문자열로 변환

print(solution(s))

print(sorted(s, reverse=True))