import sys
sys.stdin = open('2559_input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split())) 

tmp = sum(arr[:K])
result = tmp 

for i in range(K, N): 
    tmp += arr[i] - arr[i-K] 
    result = max(result, tmp) 
print(result)



# N, K = map(int, input().split())
# temp = list(map(int, input().split()))

# sum_lst = []

# for i in range(N-K+1):
#     sum_lst.append(sum(temp[i:i+K]))

# print(max(sum_lst))
