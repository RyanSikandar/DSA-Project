from json import load

# a reusable function that takes a list of words and returns a dictionary where the keys are the words and the values are the IDS
def Lexicon(word_list):
    # a list that will be returned
    word_ids = []
    # opening the lexicon json file
    with open("lexicon.json", "r") as LexiconFile:
        # loading the file in a dictionary
        lexiconDict = load(LexiconFile)
        # iterates through each word in the incoming list
        for word in word_list:
            # appends the word id to the list
            word_ids.append(lexiconDict[word])
    #returns the list
    return word_ids

# print(Lexicon(["babylon", "bee", "best", "sketch", "develop"]))
