import json

# Load the original dataset
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Iterate through the dataset and extract 'title' and 'url' for each doc_id
updated_data = {}
for doc_id, doc_info in data.items():
    updated_data[doc_id] = {
        'title': doc_info['title'],
        'url': doc_info['url']
    }

# Save the updated dataset to a new file
with open('updated_dataset.json', 'w') as updated_file:
    json.dump(updated_data, updated_file, indent=2)
