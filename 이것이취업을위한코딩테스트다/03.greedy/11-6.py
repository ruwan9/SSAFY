food_times = [3, 1, 2]	
k = 5

#################### 방법 1 ####################
# 테스트 케이스에서 실패가 몇개 나온다... 0일때 다음거로 넘어가는 부분을 더 생각해봐야할 듯


# def test(food_times, time):
# 	global tmp
# 	tmp = (time % len(food_times))
# 	if food_times[tmp] != 0:
# 		food_times[tmp] -= 1
# 		time += 1
# 		return tmp
# 	if food_times[tmp] == 0:
# 		test(food_times, time+1)

# time = 0
# while time <= k:
# 	tmp = time % len(food_times)

# 	if food_times[tmp] == 0:
# 		tmp = test(food_times, time)
# 		time += 1
# 	else:
# 		food_times[tmp] -= 1
# 		time += 1

# 	print(time, tmp, food_times)

time = 0
while time <= k:
	tmp = time % len(food_times)

	if food_times[tmp] == 0:
		tmp = (tmp+1)%len(food_times)
		food_times[tmp] -= 1
		time += 1
	else:
		food_times[tmp] -= 1 
		time += 1

	print(time, tmp, food_times)

foods = [i+1 for i in range(len(food_times))]


print(foods[tmp])


#################### 방법 2 ####################
# import heapq

# def solution(food_tims, k):
# 	# 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 return
# 	if sum(food_times) <= k:
# 		return -1

# 	# 시간이 작은 음식부터 빼기: 우선순위 큐
# 	q = []
# 	for i in range(len(food_times)):
# 		# (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
# 		heapq.heappush(q, (food_times[i], i + 1))

# 	sum_value = 0  # 먹기 위해 사용한 시간
# 	previous = 0  # 직전에 다 먹은 음식 시간

# 	length = len(food_times)  # 남은 음식 개수

# 	# sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
# 	while sum_value + ((q[0][0] - previous) * length) <= k:
# 		now = heapq.heappop(q)[0]
# 		sum_value += (now - previous) * length
# 		length -= 1  # 다 먹은 음식 제외
# 		previous = now  # 이전 음식 시간 재설정

# 	# 남은 음식 중 몇 번째 음식인지 확인하여 출력
# 	result = sorted(q, key = lambda x: x[1])  # 음식 번호 기준으로 정렬
# 	return result[(k - sum_value) % length][1]

# print(solution(food_times, k))

"""
우선순위 큐, heapq
"""