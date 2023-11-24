from os import listdir
from json import load, dumps, loads

# Retrieves the list of all the JSON files containing the articles
JSONS = listdir("articles")

# A list to store all the articles
allArticles = []

for JSON in JSONS:
    # opens each file one by one
    with open("articles/" + JSON, "r") as article_file:
        # loads the json format in Python Data Structure Format
        articles = load(article_file)
        # appends the dict to the list containing all of the articles
        for article in articles:
            allArticles.append(article)


# creates a file to store all the articles and writes the JSON to the file
with open("allArticles.json", "w") as Dataset:
    Dataset.write(dumps(articles))