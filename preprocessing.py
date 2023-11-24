#Give numbers to ids
#Source, title and content are to be prepocessed
#Remove stop words
#Stemming
#Tokenize




# {
#     "id": "21stcenturywire--2022-01-01--Babylon Bee \u2013 The Best Sketches of 2021",
#     "date": "2022-01-01",
#     "source": "21stcenturywire",
#     "title": "Babylon Bee \u2013 The Best Sketches of 2021",
#     "content": "Looking back at 2021 , here is a highlight reel of some of the best sketches from the politically incorrect @ @ @ @ @ .\nWatch : PLEASE HELP SUPPORT OUR INDEPENDENT MEDIA PLATFORM HERE",
#     "author": "NEWS WIRE",
#     "url": "https://21stcenturywire.com/2022/01/01/the-best-babylon-bee-sketches-of-2021/",
#     "published": "Sat, 01 Jan 2022 16:31:37 +0000",
#     "published_utc": 1641072697,
#     "collection_utc": 1641078005
# }



#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
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

        # Perform stemming on content
        content_stemmed = []
        for word in content_filtered:
            if word not in unwanted_tokens:
                content_stemmed.append(ps.stem(word))

        # Perform stemming on title
        title_stemmed = []
        for word in title_filtered:
            title_stemmed.append(ps.stem(word))

        # Update object with processed content and title
        obj['content'] = ' '.join(content_stemmed)
        obj['title'] = ' '.join(title_stemmed)

        processed_objects.append(obj)

    return processed_objects

# Example usage (same as before)
data = [
    {
        "id": "21stcenturywire--2022-01-01--Babylon Bee \u2013 The Best Sketches of 2021",
        "date": "2022-01-01",
        "source": "21stcenturywire",
        "title": "Babylon Bee \u2013 The Best Sketches of 2021",
        "content": "Looking back at 2021 , here is a highlight reel of some of the best sketches from the politically incorrect @ @ @ @ @ .\nWatch : PLEASE HELP SUPPORT OUR INDEPENDENT MEDIA PLATFORM HERE",
        "author": "NEWS WIRE",
        "url": "https://21stcenturywire.com/2022/01/01/the-best-babylon-bee-sketches-of-2021/",
        "published": "Sat, 01 Jan 2022 16:31:37 +0000",
        "published_utc": 1641072697,
        "collection_utc": 1641078005
    },
{
        "id": "21stcenturywire--2022-01-01--Babylon Bee \u2013 The Best Sketches of 2021",
        "date": "2022-01-01",
        "source": "21stcenturywire",
        "title": "Babylon Bee \u2013 The Best Sketches of 2021",
        "content": "Looking back at 2021 , here is a highlight reel of some of the best sketches from the politically incorrect @ @ @ @ @ .\nWatch : PLEASE HELP SUPPORT OUR INDEPENDENT MEDIA PLATFORM HERE",
        "author": "NEWS WIRE",
        "url": "https://21stcenturywire.com/2022/01/01/the-best-babylon-bee-sketches-of-2021/",
        "published": "Sat, 01 Jan 2022 16:31:37 +0000",
        "published_utc": 1641072697,
        "collection_utc": 1641078005
    },
    {
        "id": "anotherID--2022-02-02--Another Title",
        "date": "2022-02-02",
        "source": "someSource",
        "title": "Another Title",
        "content": "This is another piece of content with different words and ideas. @ @ @ @ @",
        "author": "Another Author",
        "url": "https://someurl.com",
        "published": "Wed, 02 Feb 2022 12:00:00 +0000",
        "published_utc": 1643817600,
        "collection_utc": 1643821200
    },
    {
        "id": "thirdID--2022-03-03--Third Entry",
        "date": "2022-03-03",
        "source": "thirdSource",
        "title": "Third Entry",
        "content": "The third entry has its own unique content and ideas that differ from the rest. @ @ @ @ @",
        "author": "Third Author",
        "url": "https://thirdurl.com",
        "published": "Thu, 03 Mar 2022 08:00:00 +0000",
        "published_utc": 1646308800,
        "collection_utc": 1646312400
    }
]

 # opens each file one by one
with open("allArticles.json", "r") as article_file:
        # loads the json format in Python Data Structure Format
        articles = load(article_file)

processed_articles = process_objects(articles)
count = 0


# for article in articles:
#     if count < 1:
#         print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")
#         print(article['content_processed'])
#         print(article['title_processed'])
#         count += 1

with open("allArticles.json", "w") as dataset:
    dataset.write(dumps(processed_articles))

