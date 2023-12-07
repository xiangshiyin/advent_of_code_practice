import os
import re

os.chdir(os.path.dirname(__file__))

# read the input file
with open("20231205_input.txt", "r") as file:
    input = file.read()
blobs = re.split("\n[^\n]+:", input)
# print(blobs)
print(len(blobs))

# clean seeds
seeds = [int(v) for v in blobs[0].lstrip("seeds:").strip().split()]

# clean the maps
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


# find the soils
print(f"Number of seeds: {len(seeds)}")


def find_match(inputs, a2b_map):
    outputs = []
    for input in inputs:
        found = 0
        output = -1
        for row in a2b_map:
            if input >= row[1] and input < row[1] + row[2]:
                output = row[0] + input - row[1]
                found = 1
                break
        if found == 0:
            output = input
        outputs.append(output)
    return outputs


def find_match2(intervals, a2b_map):
    outputs = []
    for interval in intervals:
        found = 0
        output = -1
        for row in a2b_map:
            
        outputs.append(output)
    return outputs


# seeds recalculated
seeds2 = []
for i in range(0, len(seeds), 2):
    seeds2.append([seeds[i], seeds[i] + seeds[i + 1] - 1])
print(f"initial seeds: {seeds}")
print(f"final seeds: {seeds2}")
print(len(seeds2))

# soils = find_match(seeds2, seed_to_soil_map)
# fertilizers = find_match(soils, soil_to_fertilizer_map)
# waters = find_match(fertilizers, fertilizer_to_water_map)
# lights = find_match(waters, water_to_light_map)
# temperatures = find_match(lights, light_to_temperature_map)
# humidities = find_match(temperatures, temperature_to_humidity_map)
# locations = find_match(humidities, humidity_to_location_map)
# print(locations)
# print(min(locations))
