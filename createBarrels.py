import json
import os

# Create a directory for barrels if it doesn't exist
if not os.path.exists("barrels"):
    os.makedirs("barrels")

# Read data from the invertedIndex.json file
with open('invertedIndex.json', 'r') as file:
    data = json.load(file)

# Iterate through the sorted keys in batches of 2500 and create barrels
barrel_count = 1
object_count = 0
objects = {}

for key in data.keys():
    objects[key] = data[key]
    object_count += 1

    # If 2500 objects are reached or it's the last object, create a barrel
    if object_count == 2500 or key == list(data.keys())[-1]:
        barrel_file_name = f"barrels/{list(objects.keys())[0]}-{list(objects.keys())[-1]}.json"
        with open(barrel_file_name, 'w') as barrel_file:
            json.dump(objects, barrel_file, indent=4)
        # Reset variables for the next barrel
        object_count = 0
        objects = {}
        barrel_count += 1