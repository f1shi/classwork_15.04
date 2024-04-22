globalCount = 0
for i in range(1, 300):
    count = 0
    for j in range(1, i):
        if i // j:
            count += 1
    if count == 5:
        globalCount += 1
print(globalCount)