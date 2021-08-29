# n = int(input())
# dices = [list(map(int, input().split())) for _ in range(n)]

n = 5
dices = [[2, 3, 1, 6, 5, 4],
        [3, 1, 2, 4, 6, 5],
        [5, 6, 4, 1, 3, 2],
        [1, 3, 6, 2, 4, 5],
        [4, 1, 6, 5, 2, 3]]

route = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
ans = 0

for i in range(6):
    res = []
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(dices[0][i])
    nxt = dices[0][route[i]]
    temp.remove(nxt)
    res.append(max(temp))

    for j in range(1, n):
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(nxt)
        nxt = dices[j][route[dices[j].index(nxt)]]
        temp.remove(nxt)
        res.append(max(temp))
    res = sum(res)

    if ans < res:
        ans = res

print(ans)


# solution 2
import sys
sys.stdin = open('2166_input.txt')
n = int(input())
dices = [[] for _ in range(n)]
answer = 0
for idx in range(n):
    nums = list(map(int, input().split()))

    dices[idx].append((nums[0],nums[5]))
    dices[idx].append((nums[1],nums[3]))
    dices[idx].append((nums[2],nums[4]))

print(dices)

def solv():
    for dice in dices[0]:
        for target in dice:
            select_num(target)
    print(answer)

def select_num(target):
    global answer
    total = 0
    for idx in range(n):
        for dice in dices[idx]:
            if target in dice:
                if 6 in dice:
                    if 5 in dice:
                        total += 4
                    else:
                        total += 5
                else:
                    total += 6
                if target == dice[0]:
                    target = dice[1]
                    break
                else:
                    target = dice[0]
                    break
    answer = max(answer,total)
solv()