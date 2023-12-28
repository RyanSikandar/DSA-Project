import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from json import load, dumps, loads, dump

nltk.download('punkt')
nltk.download('stopwords')

def process_articles(articles):
    # get a set of all the predefined stop words of English language
    stop_words = set(stopwords.words('english'))
    # creates a stemmer object
    ps = PorterStemmer()

    # a list to store the processed articles
    processed_articles = []

    id = 1

    # handles all the articles one by one, updates its title and content, and stores it in the list
    for article in articles:
        # Tokenize content and title
        content_tokens = word_tokenize(article['content'])
        title_tokens = word_tokenize(article['title'])

        # Remove stop words from content
        content_filtered = []
        for word in content_tokens:
            if word.lower() not in stop_words:
                content_filtered.append(word)

        # Remove stop words from title
        title_filtered = []
        for word in title_tokens:
            if word.lower() not in stop_words:
                title_filtered.append(word)

        # tokens that we don't need for query processing such as punctuations and special symbols
        unwanted_tokens = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        # Perform stemming on content
        content_stemmed = []
        for word in content_filtered:
            if word not in unwanted_tokens:
                content_stemmed.append(ps.stem(word))

        # Perform stemming on title
        title_stemmed = []
        for word in title_filtered:
            if word not in unwanted_tokens:
                title_stemmed.append(ps.stem(word))

        # Update article with processed content and title
        article['content'] = ' '.join(content_stemmed)
        article['title'] = ' '.join(title_stemmed)
        
        # store the length of the article by adding the lengths of the lists containing content and title
        article["length"] = len(content_stemmed) + len(title_stemmed)
        processed_articles.append(article)

        id += 1

    return processed_articles

 # opens each file one by one
with open("dataset.json", "r") as article_file:
        # loads the json format in Python Data Structure Format
        articles = load(article_file)
                                                                                                                                                                                                         
processed_articles = process_articles(articles)

with open("dataset.json", "w") as dataset:
    dump(processed_articles, dataset)
