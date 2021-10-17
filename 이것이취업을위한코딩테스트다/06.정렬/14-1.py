import sys
sys.stdin = open('input14-1.txt')

N = int(input())
infos = []
for _ in range(N):
    infos.append(list(input().split()))
print(infos)

# 기본적으로 sort는 순서대로 인자를 확인하며 오름차순 정렬
# lambda를 이용해 idx에 따라 오름/내림차순 확인
infos.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for info in infos:
    print(info[0])