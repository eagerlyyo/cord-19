PUNCTUATIONS = '!"#$%&()*+,-/:;<=>?@[\\]^_`{|}~\t\n'
REPLACE = ' '*len(PUNCTUATIONS)

def getSentences(para):
    return para.split("\n")

def getSentencesDotSeparated(para):
    replaceMap = para.maketrans(PUNCTUATIONS,REPLACE)
    para = para.translate(replaceMap)
    return para.lower().split(". ")