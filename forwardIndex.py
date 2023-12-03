from nltk.tokenize import word_tokenize
from json import load, dumps
from LexiconModule import Lexicon

# make an empty dictionary containing the forward index
forwardIndex = {}

# open the json file containing all of the articles
with open("dataset.json", "r") as dataset:
    # load the articles in a dictionary
    articles = load(dataset)
    # iterate through each of the articles
    for article_id, article in articles.items():                                                    #ARTICLE
        # extract a list of the word ids in the title of the article
        content_words_ids = Lexicon(word_tokenize(article["content"]))
        # extract a list of the word ids in content of the article
        title_words_ids = Lexicon(word_tokenize(article["title"]))
        # create an empty dictionary in the forward index for the current article id
        forwardIndex[article_id] = {}
        # set the weightage of each word in the document to 0
        for word_id in title_words_ids:
            forwardIndex[article_id][word_id] = [0, []]
        for word_id in content_words_ids:
            forwardIndex[article_id][word_id] = [0, []]
        # add 25 to the weightage score for a word occuring in the title of the article and add -1 to the hitlist
        for word_id in title_words_ids:
            forwardIndex[article_id][word_id][0] += 25
            forwardIndex[article_id][word_id][1].append(-1)
        for index, word_id in enumerate(content_words_ids):
            # add 10 to the weightage score for a word occuring in the first 30 words of the content of the article
            if index < 30:
                forwardIndex[article_id][word_id][0] += 10
            # add 5 to the weightage score for a word occuring between postions 30 and 70 in the content of the article
            elif index < 70:
                forwardIndex[article_id][word_id][0] += 5
            # add 5 to the weightage score for a word occuring between postions 70 and 150 in the content of the article
            elif index < 150:
                forwardIndex[article_id][word_id][0] += 2
            # add 1 to the weightage score for a word occuring after postion 150 in the content of the article
            else:
                forwardIndex[article_id][word_id][0] += 1
            # add the position of occurence of the word in the hitlist
            forwardIndex[article_id][word_id][1].append(index)

# write the forward index to a json file
with open("forwardIndex.json", "w") as ForwardIndex:
    ForwardIndex.write(dumps(forwardIndex))




