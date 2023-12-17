from json import load

# a reusable function that takes a list of words and returns a dictionary where the keys are the words and the values are the IDS
def Lexicon(word_list):
    # a list that will be returned
    word_ids = []
    # opening the lexicon json file
    with open("lexicon.json", "r") as LexiconFile:
        # loading the file into a dictionary
        lexiconDict = load(LexiconFile)
        # iterates through each word in the incoming list
        for word in word_list:
            # appends the word id to the list
            # using get() to handle missing words by providing a default value of -1
            word_ids.append(lexiconDict.get(word.lower(), -1))
    # returns the list
    return word_ids

def lexicon(word):
    # opening the lexicon json file
    with open("lexicon.json", "r") as LexiconFile:
        # loading the file into a dictionary
        lexiconDict = load(LexiconFile)
        # using get() to handle missing words by providing a default value of -1
        return (lexiconDict.get(word.lower(), -1))
