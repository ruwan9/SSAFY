a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

tot = 0
for i in range(len(a)):
    tot += a[i]*b[i]
print(tot)