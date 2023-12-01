from nltk.tokenize import word_tokenize
from json import load, dumps
from LexiconModule import Lexicon

# make an empty dictionary containing the forward index
forwardIndex = {}

i = 1
# open the json file containing all of the articles
with open("dataset.json", "r") as dataset:
    # load the articles in a dictionary
    articles = load(dataset)
    # iterate through each of the articles
    for article in articles:
        if(i > 2):
            break                                                                   #ARTICLE
        # extract a list of the word ids in the title of the article
        content_words_ids = Lexicon(word_tokenize(article["content"]))
        # extract a list of the word ids in content of the article
        title_words_ids = Lexicon(word_tokenize(article["title"]))
        # create an empty dictionary in the forward index for the current article id
        forwardIndex[article["id"]] = {}
        # create empty arrays in the nested dictionary for each distinct word id
        for word_id in title_words_ids:                                              #Word in Title of an article
            forwardIndex[article["id"]][title_words_ids[word_id]] = []
        for word_id in content_words_ids:                                            #Word in content of an article
            forwardIndex[article["id"]][content_words_ids[word_id]] = []
        # add a '0' in the hit list for a word occuring in the title of the article
        for word_id in title_words_ids:
            forwardIndex[article["id"]][title_words_ids[word_id]].append(-1)
        # add the postion of the word occuring in the content of the article in the hit list
        for index, word_id in enumerate(content_words_ids):
            forwardIndex[article["id"]][content_words_ids[word_id]].append(index)
        i += 1
# write the forward index to a json file
with open("forwardIndex.json", "w") as ForwardIndex:
    ForwardIndex.write(dumps(forwardIndex))

