from os import listdir
from json import load, dumps, loads

# Retrieves the list of all the JSON files containing the articles
JSONS = listdir("articles")

# A list to store all the articles
allArticles = []

counter = 0

for JSON in JSONS:
    with open("articles/" + JSON, "r") as article_file:
        articles = load(article_file)
        # Load the JSON content from the file
        for article in articles:
            allArticles.append(article)


with open("allArticles.json", "w") as Dataset:
    Dataset.write(dumps(articles))
