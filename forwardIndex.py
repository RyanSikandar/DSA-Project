from nltk.tokenize import word_tokenize
from json import load, dumps, dump
from LexiconModule import Lexicon
import time
import hashlib
import os

# Create a forward barrels folder if it doesn't exist
# if not os.path.exists("forward_barrels"):
#     os.makedirs("forward_barrels")

# make an empty dictionary containing the forward index
forwardIndex = {}

counter = 0
file_number = 1

start = time.time()

def calculate_word_id(word):
    word_hash = hashlib.sha256(word.encode()).hexdigest()
    return int(word_hash, 16)

title_words_ids = []

content_words_ids = []

# open the json file containing all of the articles
with open("dataset.json", "r") as dataset:
    # load the articles in a dictionary
    articles = load(dataset)
    dataset.close()
    # iterate through each of the articles
for article in articles:                                                    #ARTICLE
    #tokenize the article content
    tokenized_content = word_tokenize(article["content"])
    # tokenize the article title
    tokenized_title = word_tokenize(article["title"])
    # extract a list of the word ids in the title of the article
    for word in tokenized_title:
        title_words_ids.append(calculate_word_id(word))
    # extract a list of the word ids in content of the article
    for word in tokenized_content:
        content_words_ids.append(calculate_word_id(word))
    # create an empty dictionary in the forward index for the current article id
    forwardIndex[article["id"]] = {}
    # set the weightage of each word in the document to 0
    for word_id in tokenized_title:
        forwardIndex[article["id"]][word_id] = 0
    for word_id in tokenized_content:
        forwardIndex[article["id"]][word_id] = 0
    # add 5 to the weightage score for a word occuring in the title of the article and add -1 to the hitlist
    for word_id in tokenized_title:
        forwardIndex[article["id"]][word_id] += 5
        # forwardIndex[article["id"]][word_id][1].append(-1)                                                                                                                                                                                                                                                
    for index, word_id in enumerate(tokenized_content):
        # add to the weightage score for each occurence of the word in the document
        forwardIndex[article["id"]][word_id] += 1
        # add the position of occurence of the word in the hitlist
        # forwardIndex[article["id"]][word_id][1].append(index)
    print(counter)
    counter += 1
    # if counter >= 10000:
    #     break

    #     ForwardIndexFile.close()
    #     counter = 0
    #     file_number += 1
    #     forwardIndex = {}



#forward indexing
with open(f"forwardIndex.json", "w") as ForwardIndexFile:
    dump(forwardIndex, ForwardIndexFile)

# write the forward index to a json file
