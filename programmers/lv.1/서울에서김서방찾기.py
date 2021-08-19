seoul = ['Jane', 'Kim']

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'

print(solution(seoul))

# 2.
def find_kim(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))