from os import listdir
from json import load, dumps, loads

# Retrieves the list of all the JSON files containing the articles
JSONS = listdir("articles")

# A list to store all the articles
allArticles = []

counter = 0

for JSON in JSONS:
    if counter == 0:
        with open("articles/" + JSON, "r") as article_file:
            articles = load(article_file)
            # Load the JSON content from the file
            for article in articles:
                allArticles.append(article)
    counter += 1


with open("allArticles.json", "w") as Dataset:
    Dataset.write(dumps(articles))

# objects = []
# with open("test.json", "r") as test:
#         data_list = load(test)
        
#         for t in data_list:
#             objects.append(t)

# print(objects)

# with open("tester.json", "w") as file:
#       file.write(dumps(objects))

