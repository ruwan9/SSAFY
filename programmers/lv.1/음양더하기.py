absolutes = [4,7,12]
signs = [True,False,True]

tot = 0
for i in range(len(signs)):
    if signs[i]:
        tot += absolutes[i]
    else:
        tot -= absolutes[i]

print(tot)