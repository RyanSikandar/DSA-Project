from LexiconModule import calculate_word_id
from json import load

word = input("Enter a word to search for: ")
word_id = calculate_word_id(word)

articles = []

if word_id >= 34 and word_id <= 3704:
    with open("barrels/34-3704.json", "r") as barrel:
        invertedIndex = load(barrel)
        articlesDictionary = invertedIndex[str(word_id)]
        articles = sorted(articlesDictionary.keys(), key=lambda x: -articlesDictionary[x][0])

elif word_id >= 3705 and word_id <= 7596:
    with open("barrels/3705-7596.json", "r") as barrel:
        invertedIndex = load(barrel)
        articlesDictionary = invertedIndex[str(word_id)]
        articles = sorted(articlesDictionary.keys(), key=lambda x: -articlesDictionary[x][0])

elif word_id >= 7599 and word_id <= 42193:
    with open("barrels/7599-42193.json", "r") as barrel:
        invertedIndex = load(barrel)
        articlesDictionary = invertedIndex[str(word_id)]
        articles = sorted(articlesDictionary.keys(), key=lambda x: -articlesDictionary[x][0])

elif word_id >= 42196 and word_id <= 2676916:
    with open("barrels/42196-2676916.json", "r") as barrel:
        invertedIndex = load(barrel)
        articlesDictionary = invertedIndex[str(word_id)]
        articles = sorted(articlesDictionary.keys(), key=lambda x: -articlesDictionary[x][0])


print(articles)
