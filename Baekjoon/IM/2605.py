n = 5
arr = [0, 1, 1, 3, 2]

line = []

for i in range(1, n+1):
    line.insert(arr[i-1], i)

print(*line[::-1])
