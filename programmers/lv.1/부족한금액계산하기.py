price = 3
money = 20
count = 4

# 1
def solution(price, money, count):
    cnt = 0
    for i in range(count+1):
        cnt += i

    tot = price * cnt  # 총 내야하는 금액

    if tot > money:
        return tot - money
    else:
        return 0

# 2
def solution2(price, money, count):
    pay = 0
    for i in range(count+1):
        pay += i*price

    if pay > money:
        return pay - money
    else:
        return 0


print(solution2(price, money, count))