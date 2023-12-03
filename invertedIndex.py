from json import load, dumps

# create a dictionary to store the inverted index
invertedIndex = {}

# open the Forward Index file and read the data into a variable
with open ("forwardIndex.json", "r") as ForwardIndexFile:
    forwardIndex = load(ForwardIndexFile)
    # loop through the key value pairs in the outer dictionary
    for document_id, words_data in forwardIndex.items():
        # for each key value pair in the outer dictionary, loop through the key value pairs in the inner dictionary
        for word_id, weightageAndHitList in words_data.items():
            # if the word doesn't already exist in the inverted index, create an empty dictionary against that word id in the inverted index
            if word_id not in invertedIndex:
                invertedIndex[word_id] = {}
            # add the document id and the weightage score in the dictionary of that word id
            invertedIndex[word_id][document_id] = weightageAndHitList

with open("invertedIndex.json", "w") as InvertedIndexFile:
    InvertedIndexFile.write(dumps(invertedIndex))
