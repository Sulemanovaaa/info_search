# Please, install pymorphy2-dicts-ru

import os
import pymorphy2

# list of words
# langs as two symbol code
def lem(morph, words):
    trueWords = []
    for word in words:
        iWord = morph.parse(u"" + word)[0].normal_form
        if (len(iWord) > 0):
            trueWords.append(iWord)
    return trueWords

def main():
    morph = pymorphy2.MorphAnalyzer()
    rawDirectory = './pages'
    cleanDirectory = './lem'
    rawPaths = os.listdir(rawDirectory)
    for rawPath in rawPaths:
        uglyWords = []
        muddyFile = open(rawDirectory + '/' + rawPath, 'r')
        for line in muddyFile:
            for word in line.split():
                if isHealthyWord(word):
                    uglyWords.append(word)
        muddyFile.close()
        pureWords = lem(morph, uglyWords)

        pureFile = open(cleanDirectory + '/' + rawPath, 'w')
        pureFile.write(" ".join(pureWords))
        pureFile.close()

def isHealthyWord(word):
    return word.lower().isalpha() or word.isdigit()
    

if __name__ == "__main__":
    main()


