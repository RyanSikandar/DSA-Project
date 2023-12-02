from json import load, dumps

# Load data from forwardIndex.json
with open('forwardIndex.json', 'r') as file:
    forward_index_data = load(file)

# Initialize an empty dictionary to store the transformed data
transformed_data = {}

# Iterate through the nested dictionaries in forward_index_data
for document_id, word_data in forward_index_data.items():
    for word_id, doc_ids in word_data.items():
        # Check if the word_id already exists in transformed_data
        if word_id in transformed_data:
            transformed_data[word_id].update([int(document_id)])
        else:
            transformed_data[word_id] = {int(document_id)}
# Convert sets to tuples for the final structure
final_structure = {word_id: tuple(doc_ids) for word_id, doc_ids in transformed_data.items()}

# Print the final structure
with open("invertedIndex.json", "w") as InvertedIndex:
    InvertedIndex.write(dumps(final_structure))






# {
#   "1": {
#     "1": [-1],
#     "2": [-1],
#     "3": [-1],
#     "4": [-1, 5],
#   },
#   "2": {
#     "20": [-1, 151],
#     "2": [-1, 152],
#     "22": [-1, 27],
#     "957": [948]
#   }
# }
