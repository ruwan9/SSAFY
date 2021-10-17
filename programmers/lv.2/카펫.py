brown = 10
yellow = 2

# ans = []
# area = brown + yellow
# for row in range(brown//2):
#     for col in range(brown//2):
#         if row >= col and row * col == area:
#             ans.append(row)
#             ans.append(col)
#
# print(ans)

area = brown + yellow
for row in range(1, max(brown//2, yellow//2)):
    for col in range(1, max(brown//2, yellow//2)):
        if row >= col and row * col == area:
            print([row, col])

