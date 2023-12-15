import json

# Read data from the JSON file
with open('invertedIndex.json', 'r') as file:
    data = json.load(file)

# Sort the dictionary keys as integers and convert them back to strings
sorted_keys = sorted(data.keys(), key=lambda x: int(x))

# Create a new dictionary with sorted keys
sorted_data = {str(key): data[str(key)] for key in sorted_keys}

# Write the sorted data back to the JSON file
with open('invertedIndex.json', 'w') as file:
    json.dump(sorted_data, file, indent=4)