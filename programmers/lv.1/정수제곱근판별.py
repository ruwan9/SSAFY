n = 121

# 1
def solution(n): 
    x = 1
    while x <= n**0.5:
        if x**2 == n:
            return (x+1)**2
        else:
            x += 1
    return -1

print(solution(n))

# 2
from math import sqrt

def solution(n):
    return int(sqrt(n)+1)**2 if sqrt(n)%1 == 0 else -1

print(solution(n))