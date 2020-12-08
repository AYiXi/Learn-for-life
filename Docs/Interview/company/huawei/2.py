min_average_lost = 2
# 0-1 3-4 6-7
losts = [0, 0, 100, 2, 2, 99, 0, 2]
lost_len = len(losts)

indexes = []
for index, lost in enumerate(losts):
    length = 0
    l = [lost]
    for i in range(index + 1, lost_len):
        total = l + [losts[i]]
        if sum() / len(l + [losts[i]]) > 2:
            indexes.append([index, i - 1, length])
            break
        l.append()
        length += 1

print(indexes)
    