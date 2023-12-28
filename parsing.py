from os import listdir
from json import load, dumps, loads, dump

# Retrieves the list of all the JSON files containing the articles
JSONS = listdir("articles")

# A list to store all the articles
allArticles = []

# a unique integral id to assign to each of the articles
id = 1

print(JSONS)

for JSON in JSONS:
    print(JSON)

for JSON in JSONS:
    # opens each file one by one
    with open("articles/" + JSON, "r") as article_file:
        # loads the json format in Python Data Structure Format
        articles = load(article_file)
        # appends the dict to the list containing all of the articles
        for article in articles:
            article["id"] = id
            # add the article to the list containing all of the parsed articles
            allArticles.append(article)
            # increments the id counter
            id += 1
    if id >= 15000:
        break

# creates a file to store all the articles and writes the JSON to the file
with open("dataset.json", "w") as Dataset:
    dump(allArticles, Dataset)
