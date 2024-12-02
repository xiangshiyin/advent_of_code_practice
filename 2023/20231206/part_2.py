time_limits = 45988373
distances = 295173412781210

# time_limits = 71530
# distances = 940200


first_speed = 0
for speed in range(1, time_limits):
    if speed * (time_limits - speed) > distances:
        first_speed = speed
        break

answer = time_limits - first_speed - first_speed + 1


print(f"Answer: {answer}")