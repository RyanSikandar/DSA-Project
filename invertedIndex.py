from json import load, dumps

invertedIndex = {}

# open the Forward Index file and read the data into a variable
with open ("forwardIndex.json", "r") as ForwardIndexFile:
    forwardIndex = load(ForwardIndexFile)
    for document_id, words_data in forwardIndex.items():
        for word_id, hitlist in words_data.items():
            if word_id not in invertedIndex:
                invertedIndex[word_id] = {}
            invertedIndex[word_id][document_id] = hitlist

with open("invertedIndex.json", "w") as InvertedIndexFile:
    InvertedIndexFile.write(dumps(invertedIndex))
