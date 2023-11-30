from nltk.tokenize import word_tokenize
from json import load, dumps
from LexiconModule import Lexicon

forwardIndex = {
    "1": {
        "2": [-1, 24]
    }
}

with open("dataset.json", "r") as dataset:
    articles = load(dataset)
    i = 0
    for article in articles:
        if i >= 5:
            break
        content_words_ids = Lexicon(word_tokenize(article["content"]))
        title_words_ids = Lexicon(word_tokenize(article["title"]))
        forwardIndex[article["id"]] = {}
        for word_id in title_words_ids:
            forwardIndex[article["id"]][word_id] = []
        for word_id in content_words_ids:
            forwardIndex[article["id"]][word_id] = []
        for word_id in title_words_ids:
            forwardIndex[article["id"]][word_id].append(0)
        for index, word_id in enumerate(content_words_ids):
            forwardIndex[article["id"]][word_id].append(index)

print(forwardIndex)

with open("forwardIndex.json", "w") as ForwardIndex:
    ForwardIndex.write(dumps(forwardIndex))