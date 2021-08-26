array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    ans = []
    new_arr = []
    
    for i in range(len(commands)):
        new_arr = sorted(array[commands[i][0]-1:commands[i][1]])
        ans.append(new_arr[commands[i][2]-1])
    
    return ans

# 2
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

