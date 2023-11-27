forwardIndex = {
    "2": {
        "32": [29, 92],
        "92": [100, 101]
    },
    "3": {
        "10": [912, 24],
        "25": [10]
    }
}

# brutus caesar

invertedIndex = {
    "brutus": {
        "2": [20, 21],
        "3": [50, 22]
    }, 
    "caesar": {
        "3": [51, 23],
        "2": [100, 140],
        
    }
}

#Forward Index
forwardIndex = {
    "1" : [
        {
            "word" : 10,
            "weight" : 2,
            "location" : [15, 70]
        },
        {
            "word" : 56,
            "weight" : 1,
            "location" : [ 20 ]
        }
    ],
    "2" : [
        {
            "word" : 10,
            "weight" : 1,
            "location" : [ 90, 69 ]
        }
    ]
}

#Inverted Index

Brutus --> 19
Caeser --> 25

invertedIndex = {
    "brutus": {
        "2": [20, 21],
        "3": [50, 22]
    }, 
    "caesar": {
        "3": [51, 23],
        "2": [100, 140],
        
    }
}

def calc_score(doc):
    score = 0
    return score

results = {"1": 50}

documents = {}

words = ["brutus", "caesar"]

for word in words:
    documents.append(invertedIndex[word])





docs = documents.keys() #list of keys
for doc in docs:
    results[doc] = calc_score(doc)
    



invertedIndex = {           
    "19" : [
        {
            "doc" : 1,
            "weight" : 3,
            "location" : [15, 70, 80]
        },
        {
            "doc" : 3,
            "weight" : 4,
            "location" : [ 2, 10, 17, 25]
        }
    ],
    "25" : [
        {
            "doc" : 1,
            "weight" : 2,
            "location" : [ 19, 87 ]
        }
    ]
}

docs1 = invertedIndex["25"]
docs2 = invertedIndex["19"]


docs.append(docs1)
docs.append(docs2)
# docs = [[.......], [......]]

for doc in docs


for document in docs
    calcScore(document.doc)


#[[1, 2, 3], [3, 4, 5], [3, 6, 7]]

# words = [word1, word2, word3]

# docs = ()

# i=1
# for word in words
#     if i = 1
#         docs.append(invertedIndex[word].keys())
#     else
#         #Take intersection of whatever is in docs and the new word

# Result: the intersected doc IDs

list = ()

for index in indices


#helllooo sexy ladyyyyyy.
# 1. We go through every document.
# 2. Extract words and their positions.
# 3. Store them in a dictionary where each document would be a separate dictionary
# 4. Each document will have values 