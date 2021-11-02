#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()

    # 숫자 카드를 담을 임시 리스트
    tmp = [0] * 10
    # 카드의 장 수
    max_num = 0
    # 가장 많은 카드에 적힌 숫자
    max_idx = 0

    for card in cards:
        tmp[int(card)] += 1

    # 카드의 장수가 같을 때 적힌 숫자가 큰 쪽을 출력 -> 뒤에서부터 비교
    for i in range(9, 0, -1):
        if tmp[i] > max_num:
            max_num = tmp[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_num}')



#################### 방법 2. ####################
# enumerate 사용
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    card_list = [0] * 10

    for card in cards:
        card_list[card] += 1

    max_idx = 0
    max_cnt = 0

    for idx, value in enumerate(card_list):
        # 가장 큰 인덱스로 갱신
        if value >= max_cnt:
            max_cnt = value
            max_idx = idx

    print(f'#{tc} {max_idx} {max_cnt}')



#################### 방법 3. ####################
# dict 사용
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    card_list = {i: 0 for i in range(10)}

    for card in cards:
        card_list[card] += 1

    max_cnt = 0
    max_idx = 0

    for i in range(9, -1, -1):
        if card_list[i] > max_cnt:
            max_cnt = card_list[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_cnt}')