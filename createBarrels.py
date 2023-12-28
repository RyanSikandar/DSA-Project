# import json
# import os

# # Create a directory for barrels if it doesn't exist
# if not os.path.exists("barrels"):
#     os.makedirs("barrels")

# # Read data from the invertedIndex.json file
# with open('invertedIndex.json', 'r') as file:
#     data = json.load(file)

# # Iterate through the sorted keys in batches of 2500 and create barrels
# barrel_count = 1
# object_count = 0
# objects = {}

# for key in data.keys():
#     objects[key] = data[key]
#     object_count += 1

#     # If 2500 objects are reached or it's the last object, create a barrel
#     if object_count == 2500 or key == list(data.keys())[-1]:
#         barrel_file_name = f"barrels/{list(objects.keys())[0]}-{list(objects.keys())[-1]}.json"
#         with open(barrel_file_name, 'w') as barrel_file:
#             json.dump(objects, barrel_file, indent=4)
#         # Reset variables for the next barrel
#         object_count = 0
#         objects = {}
#         barrel_count += 1



import os
import json

def create_barrels(inverted_index_data):
    # Create barrels directory if it doesn't exist
    if not os.path.exists("barrels"):
        os.makedirs("barrels")

    # Loop through word IDs in invertedIndex.json
    for word_id, value in inverted_index_data.items():
        # Get last two digits of the word ID
        barrel_number = word_id[-3:]

        # Create or update the corresponding barrel file
        barrel_filename = f"barrels/{barrel_number}.json"
        
        # Load existing barrel data if present
        if os.path.exists(barrel_filename):
            with open(barrel_filename, 'r') as file:
                barrel_data = json.load(file)
        else:
            barrel_data = {}

        # Insert the data under the corresponding barrel
        barrel_data[word_id] = value

        # Write updated data to the barrel file
        with open(barrel_filename, 'w') as file:
            json.dump(barrel_data, file)

# Load data from invertedIndex.json
with open('invertedIndex.json', 'r') as file:
    inverted_index_data = json.load(file)

# Call the function with the loaded data
create_barrels(inverted_index_data)
