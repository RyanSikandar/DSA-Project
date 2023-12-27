from json import load, dump

total_articles = 29709

# open the inverted index and load it into a dictionary
with open("invertedIndex.json", "r") as invertedIndexFile:
    invertedIndex = load(invertedIndexFile)

    with open("dataset.json", "r") as datasetFile:
        dataset = load(datasetFile)

        for word_id, doc_dictionary in invertedIndex.items():
            for doc_id, array in doc_dictionary.items():
                if doc_id != "idf":
                    array.append(array[0] / dataset[int(doc_id) - 1]["length"])
            doc_dictionary["idf"] = [total_articles, len(doc_dictionary)]

with open("invertedIndex.json", "w") as invertedIndexFile:
    dump(invertedIndex, invertedIndexFile)

# tf = number of times the term appears in the document / total number of terms in the document

#idf = number of documents in the corpus / number of documents in the corpus that contain the term



#  "2" : {
#      "a": [weightage, hitlist, tf],
#      "b": [weightage, hitlist, tf],
        # "c": 
        # "idf": [number of elements in the corpus, number of elements in the corpus that contain the term]
#  }