import sys
sys.stdin = open('input_files/1302.txt')


# #################### 방법 1. ####################
# # set() 활용
# N = int(input())
# books = list(input() for _ in range(N))
# # 중복 제거, 정렬한 책 리스트
# book_lst = sorted(list(set(books)))
#
# cnts = []
# # 팔린 책의 수를 cnts에 추가
# for book in book_lst:
#     cnts.append(books.count(book))
# # 가장 많이 팔린 책의 인덱스를 정렬한 책 리스트에서 print
# idx = cnts.index(max(cnts))
# print(book_lst[idx])
#
#
# #################### 방법 2. ####################
# # set() 활용
# N = int(input())
# books = list(input() for _ in range(N))
# # 중복 제거, 정렬한 책 리스트
# book_lst = sorted(list(set(books)))
#
# # index값과 팔린 책의 수 초기화
# max_idx = 0
# max_cnt = 0
# for i in range(len(book_lst)):
#     if books.count(book_lst[i]) > max_cnt:
#         max_idx = i
#         max_cnt = books.count(book_lst[i])
#
# print(book_lst[max_idx])


#################### 방법 3. ####################
# Dictionary 활용

N = int(input())
books = {}

for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())  # value값 중 가장 큰 값
arr = []

for book, number in books.items():
    if number == target:
        arr.append(book)  # 사전순으로 프린트해내기 위해

print(sorted(arr)[0])  # 정렬 후 제일 앞의 값 출력