from LexiconModule import Lexicon
from json import load
import time

# get the query to from the user
word = input("Enter a word to search for: ").lower()

# starting the clock
start = time.time()

#retrieving the word id from the lexicon
word_id = Lexicon(word)

# calculate the barrel index and convert it to a string
barrel_index = str(word_id % 100)

# append a 0 to the left if the barrel index is a single digit
if len(barrel_index) == 1:
    barrel_index = '0' + barrel_index

# the path to the required barrel in a string
barrel_path = "barrels/{}.json".format(barrel_index)

# lists to store article ids and urls
article_ids = []
urls = []

with open(barrel_path, "r") as barrel:
    # load the barrel in a dictionary
    inverted_index = load(barrel)
    # the dictionary stored against the wordID in the inverted index
    try:
        articlesDictionary = inverted_index[str(word_id)]
    except KeyError:
        print('No matches')
    # sort the article ids with respect to the weightage of the word in that article in descending order and save them in a list
    article_ids = sorted(articlesDictionary.keys(), key = lambda x:-articlesDictionary[x][0])

# open the dataset and retrieve the url of each article id while keeping the ranking order intact
with open('dataset.json', 'r') as datasetFile:
    dataset = load(datasetFile)
    for article_id in article_ids:
        urls.append(dataset[article_id]["url"])

#stopping the clock
end = time.time()

# printing the result
for url in urls:
    print(url)

#printing the time take in milliseconds
print("Took " + str("%.2f" % ((end - start) * 1000)) + " milliseconds")
