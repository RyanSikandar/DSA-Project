import json

# Read data from the JSON file
with open('lexicon.json', 'r') as file:
    data = json.load(file)

# Sort the dictionary by values in ascending order
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

# Write the sorted data back to the JSON file
with open('lexicon.json', 'w') as file:
    json.dump(sorted_data, file, indent=4)
