from json import load
from lexicon import calculate_word_id
import numpy as np
import time

# Load the barrel data
with open("barrels\\34-3704.json", "r") as barrel1:
    barrel = load(barrel1)

# Get user input
word_to_search = input("Enter word to search: ")
# Measure time taken to find the document with maximum value
start_time = time.time()

#Calculates the word id for the single word search
word_id = calculate_word_id(word_to_search)

word_id_string = str(word_id)

#stores the value of the word_id key
output_barrels = barrel[word_id_string]


maximum = 0
document_max = None
for key, value in output_barrels.items():
    if value[0] > maximum:
        maximum = value[0]
        document_max = key

end_time = time.time()

# Print results and time taken in milliseconds
print("Document with maximum value:")
print("Document:", document_max)
print("Maximum value:", maximum)
time_taken_ms = (end_time - start_time) * 1000  # Convert seconds to milliseconds
print(f"Time taken: {time_taken_ms:.4f} milliseconds")