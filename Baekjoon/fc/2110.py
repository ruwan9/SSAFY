import sys
sys.stdin = open('input_files/2110.txt')


N, C = map(int, input().split())
houses = sorted(list(int(input()) for _ in range(N)))
print(houses)

start = houses[1] - houses[0]  # 최대 거리
end = houses[-1] - houses[0]  # 최소 거리
res = 0

while (start <= end):
    # mid == Gap
    mid = (start + end) // 2  # 찾고자 하는 최대 거리를 mid로 두고 진행
    value = houses[0]  # 배열 중 가장 낮은 좌표
    cnt = 1
    for i in range(1, N):
        # value와의 거리가 mid 이상이면 value값 갱신
        if houses[i] >= value + mid:
            value = houses[i]
            cnt += 1
    # C개 이상의 공유기를 설치할 수 있는 경우
    if cnt >= C:
        start = mid + 1
        res = mid  # 답!
    else:
        end = mid - 1  # 왼쪽(작은 쪽) 탐색

print(res)

"""
값의 범위가 클 때 -> 이진탐색 사용
- 이진탐색을 이용하면 시간복잡도가 O(logN)

1. 최대 거리를 end값으로 둔다
2. 최소 거리를 start값으로 둔다
3. mid값을 구한다
4. 가능 여부를 확인 후 start, end값을 바꾸어 다시 확인한다
"""