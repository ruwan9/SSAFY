# 1
n, m = 4, 2 
s = []
 
def dfs():
    if len(s)==m:  # 끝
        print(*s)
        return
    
    for i in range(1,n+1):  # i = 1, 2, 3, 4
        if i not in s:  
            s.append(i)  # s에 하나 추가
            dfs()  # 재귀
            s.pop()  # 하나 제거
 
dfs()

# 2.
# n, m = 4, 2
# isused = [0] * n
# arr = []

# def dfs(idx, n, m):
#     if idx == m:  # 길이가 m이 되면 출력
#         print(*arr)
#         return
    
#     for i in range(n):
#         if isused[i] == 0:  # 사용되지 않았다면
#             isused[i] = 1  # 사용한거 체크
#             arr.append(i+1)  # 숫자 추가 (1부터 시작)
#             dfs(idx+1, n, m)  # 재귀
#             isused[i] = 0  # 사용한거 체크 해제
#             arr.pop()

# dfs(0, n, m)
