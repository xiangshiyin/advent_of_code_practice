import os
import re

os.chdir(os.path.dirname(__file__))

# read the input file
with open("20231205_input.txt", "r") as file:
    input = file.read()
blobs = re.split("\n[^\n]+:", input)
# print(blobs)
print(len(blobs))

test = 0
# clean seeds
seeds = [int(v) for v in blobs[0].lstrip("seeds:").strip().split()] if not test else [79,14,55,13]

# clean the maps
if not test:
    seed_to_soil_map = [
        [int(v) for v in row.strip().split()] for row in blobs[1].strip().split("\n")
    ]
    soil_to_fertilizer_map = [
        [int(v) for v in row.strip().split()] for row in blobs[2].strip().split("\n")
    ]
    fertilizer_to_water_map = [
        [int(v) for v in row.strip().split()] for row in blobs[3].strip().split("\n")
    ]
    water_to_light_map = [
        [int(v) for v in row.strip().split()] for row in blobs[4].strip().split("\n")
    ]   
    light_to_temperature_map = [
        [int(v) for v in row.strip().split()] for row in blobs[5].strip().split("\n")
    ]
    temperature_to_humidity_map = [
        [int(v) for v in row.strip().split()] for row in blobs[6].strip().split("\n")
    ]
    humidity_to_location_map = [
        [int(v) for v in row.strip().split()] for row in blobs[7].strip().split("\n")
    ]
else:
    seed_to_soil_map = [
        [50, 98, 2],
        [52, 50, 48]
    ]    
    soil_to_fertilizer_map = [
        [0, 15, 37],
        [37, 52, 2],
        [39, 0, 15]
    ]
    fertilizer_to_water_map = [
        [49, 53, 8],
        [0, 11, 42],
        [42, 0, 7],
        [57, 7, 4]
    ]    
    water_to_light_map = [
        [88, 18, 7],
        [18, 25, 70]
    ] 
    light_to_temperature_map = [
        [45, 77, 23],
        [81, 45, 19],
        [68, 64, 13]
    ]    
    temperature_to_humidity_map = [
        [0, 69, 1],
        [1, 0, 69]
    ]    
    humidity_to_location_map = [
        [60, 56, 37],
        [56, 93, 4]
    ]       


# seeds recalculated
seed_intervals = []
for i in range(0, len(seeds), 2):
    seed_intervals.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

def get_interval_map(a2b_map):
    interval_map = {}
    for row in a2b_map:
        interval_map.update({
            (row[1], row[1] + row[2] - 1): (row[0], row[0] + row[2] - 1)
        })
    return interval_map

seed_to_soil_map2 = get_interval_map(seed_to_soil_map)
soil_to_fertilizer_map2 = get_interval_map(soil_to_fertilizer_map)
fertilizer_to_water_map2 = get_interval_map(fertilizer_to_water_map)
water_to_light_map2 = get_interval_map(water_to_light_map)
light_to_temperature_map2 = get_interval_map(light_to_temperature_map)
temperature_to_humidity_map2 = get_interval_map(temperature_to_humidity_map)
humidity_to_location_map2 = get_interval_map(humidity_to_location_map)

counter = 0
interval_maps = [
    seed_to_soil_map2,
    soil_to_fertilizer_map2,
    fertilizer_to_water_map2,
    water_to_light_map2,
    light_to_temperature_map2,
    temperature_to_humidity_map2,
    humidity_to_location_map2
]

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
        elif interval[0] > merged_intervals[-1][1] + 1:
            merged_intervals.append(interval)
        else:
            merged_intervals.append(
                (merged_intervals.pop()[0], interval[1])
            )
    return merged_intervals

def merge_intervals_w_split(intervals, special_intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals:
            if interval not in special_intervals:
                merged_intervals.append(interval)
        elif interval[0] > merged_intervals[-1][1]:
            if interval not in special_intervals:
                merged_intervals.append(interval)
        else:
            to_break = merged_intervals.pop()
            if interval[1] > to_break[1]:
                merged_intervals.append(
                    (to_break[0], interval[0] - 1)
                )
                merged_intervals.append(
                    (interval[0], to_break[1])
                )
                # merged_intervals.append(
                #     (to_break[1] + 1, interval[1])  
                # )
            else:
                merged_intervals.append(
                    (to_break[0], interval[0] - 1)
                )
                merged_intervals.append(
                    (interval[0], interval[1])
                )
                merged_intervals.append(
                    (interval[1] + 1, to_break[1])  
                )
    return merged_intervals

def match_intervals(source_intervals, interval_map):
    # print(f"Interval map: {interval_map}")
    print(f"source_intervals: {sorted(source_intervals, key=lambda x: x[0])}")
    special_source_intervals = list(interval_map.keys())
    print(f"special_source_intervals: {sorted(special_source_intervals, key=lambda x: x[0])}")

    combined_intervals = sorted(source_intervals + special_source_intervals, key=lambda x: x[0])
    # print(f"combined_intervals: {combined_intervals}")
    merged_intervals = sorted(merge_intervals_w_split(combined_intervals, special_source_intervals), key=lambda x: x[0])
    print(f"merged_intervals: {merged_intervals}")  
    mapped_intervals = []

    for interval in merged_intervals:
        matched = 0
        # print(f"interval: {interval}")
        for interval2 in interval_map:
            if interval[0] >= interval2[0] and interval[1] <= interval2[1]:
                mapped_intervals.append(
                    (
                        interval_map[interval2][0] + interval[0] - interval2[0],
                        interval_map[interval2][0] + interval[1] - interval2[0]
                    )
                )
                matched = 1
                break
        if not matched:
            mapped_intervals.append(interval)
        # print(f"mapped_intervals: {mapped_intervals}")
    # mapped_intervals = sorted(merge_intervals(mapped_intervals), key=lambda x: x[0])
    return mapped_intervals

soil_intervals = match_intervals(seed_intervals, seed_to_soil_map2)
# print(f"Original seed intervals: {sorted(seed_intervals, key=lambda x: x[0])}")
print(f"Processed soil intervals: {soil_intervals}")

fertilizer_intervals = match_intervals(soil_intervals, soil_to_fertilizer_map2)
print(f"Processed fertilizer intervals: {fertilizer_intervals}")

water_intervals = match_intervals(fertilizer_intervals, fertilizer_to_water_map2)
print(f"Processed water intervals: {water_intervals}")

light_intervals = match_intervals(water_intervals, water_to_light_map2)
print(f"Processed light intervals: {light_intervals}")

temperature_intervals = match_intervals(light_intervals, light_to_temperature_map2)
print(f"Processed temperature intervals: {temperature_intervals}")

humidity_intervals = match_intervals(temperature_intervals, temperature_to_humidity_map2)
print(f"Processed humidity intervals: {humidity_intervals}")

location_intervals = match_intervals(humidity_intervals, humidity_to_location_map2)
print(f"Processed location intervals: {location_intervals}")

min_location = min([v[0] for v in location_intervals])
print(f"The answer is {min_location}")
