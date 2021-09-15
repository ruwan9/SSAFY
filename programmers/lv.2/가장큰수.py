# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]	

#  2. 
num = list(map(str, numbers))
num.sort(key = lambda x : x*3, reverse = True)  # 1000 이하이므로 3자리 수로 맞춘 뒤 비교
print(str(int(''.join(num))))

"""
문자열 비교 시 1000 이하이므로 3자리수로 맞춘 뒤 비교
"""