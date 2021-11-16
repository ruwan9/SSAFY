#################### 방법 1. ####################
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations_idx = list(map(int, input().split()))

    stations = [0] * (N+1)
    # 정류장 위치
    for i in stations_idx:
        stations[i] = 1

    cnt = 0  # 충전횟수
    bus = K  # 이동중인 버스 idx
    stopped = 0  # 직전에 충전한 정류장

    while bus < N:
        if stations[bus] == 1:
            cnt += 1
            stopped = bus
            bus += K
        else:
            bus -= 1  # 한칸씩 뒤로 가며 충전소 유무 확인
            # 한칸씩 뒤로 가다가 이전 정류장을 만나버리면 충전기 설치 잘못됨(종점 도착 불가)
            if bus == stopped:
                cnt = 0
                break

    print(f'#{tc} {cnt}')


#################### 방법 2. ####################
import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    now = 0  # 현 위치 인덱스
    cnt = 0  # 충전 횟수

    while now+K < N:
        for n in range(now+K, now, -1):  # 가장 먼 도착지부터 뒤로 탐색한다.
            if n in charges:  # 정류장을 만났다면 이동한다
                cnt += 1
                now = n
                break
        else:  # for문을 완료했다 = 다음 정류장을 찾지 못했다
            cnt = 0
            break

    print(f'#{tc} {cnt}')