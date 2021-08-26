nums = [3,1,2,3]

def solution(nums):
    pick = len(nums)//2
    nums = list(set(nums))  # 중복 제거

    if len(nums) < pick:
        return len(nums)
    else:
        return pick

