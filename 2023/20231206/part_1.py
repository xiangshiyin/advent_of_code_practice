times = [45, 98, 83, 73]
distances = [295, 1734, 1278, 1210]

ways = []

for i in range(len(times)):
    counter = 0
    interval = times[i]
    for speed in range(1, interval):
        if speed * (interval - speed) > distances[i]:
            counter += 1
    ways.append(counter)
print(ways)

anser = 1
for way in ways:
    anser *= way

print(f"Answer: {anser}")