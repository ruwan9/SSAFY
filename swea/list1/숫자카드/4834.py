import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 숫자 카드를 담을 임시 리스트
    tmp = [0] * 10
    # 카드의 장 수
    max_num = 0
    # 가장 많은 카드에 적힌 숫자
    max_idx = 0

    N = int(input())
    cards = input()

    for card in cards:
        tmp[int(card)] += 1

    # 카드의 장수가 같을 때 적힌 숫자가 큰 쪽을 출력 -> 뒤에서부터 비교
    for i in range(9, 0, -1):
        if tmp[i] > max_num:
            max_num = tmp[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_num}')