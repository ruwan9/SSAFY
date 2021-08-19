strings = ["sun", "bed", "car"]
n = 1

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])

print(solution(strings, n))