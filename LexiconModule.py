from json import load

# a reusable function that takes a list of words and returns a dictionary where the keys are the words and the values are the IDS
def Lexicon(word_list):
    # a dictionary that will be returned
    word_id_dict = {}
    # opening the lexicon json file
    with open("lexicon.json", "r") as LexiconFile:
        # loading the file in a dictionary
        lexiconDict = load(LexiconFile)
        # iterates through each word in the incoming list
        for word in word_list:
            # creates a key value pair extracting the ID of the word from the larger lexicon
            word_id_dict[word] = lexiconDict[word]
    #returns the dictionary
    return word_id_dict

# print(Lexicon(["babylon", "bee", "best", "sketch", "develop"]))