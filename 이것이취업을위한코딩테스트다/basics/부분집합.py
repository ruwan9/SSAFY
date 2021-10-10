arr = [1, 2, 3, 4]
N = len(arr)
subset = []

def sub(idx):
    if idx == N:
        print(subset)
        return

    subset.append(arr[idx])
    sub(idx+1)
    
    subset.pop()
    sub(idx+1)
sub(0)