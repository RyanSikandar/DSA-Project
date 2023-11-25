import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from json import load, dumps, loads

nltk.download('punkt')
nltk.download('stopwords')

def process_objects(obj_array):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    processed_objects = []

    for obj in obj_array:
        # Tokenize content and title
        content_tokens = word_tokenize(obj['content'])
        title_tokens = word_tokenize(obj['title'])

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

        unwanted_tokens = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        # Perform stemming on title
        title_stemmed = []
        for word in title_filtered:
            title_stemmed.append(ps.stem(word))

        # Update object with processed content and title
        obj['content'] = ' '.join(content_stemmed)
        obj['title'] = ' '.join(title_stemmed)

        processed_objects.append(obj)

    return processed_objects

 # opens each file one by one
with open("allArticles.json", "r") as article_file:
        # loads the json format in Python Data Structure Format
        articles = load(article_file)

processed_articles = process_objects(articles)

with open("allArticles.json", "w") as dataset:
    dataset.write(dumps(processed_articles))

