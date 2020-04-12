import numpy as np
import string

def noobEmbedding(sentence, context):
    embedding = np.zeros(26)
    for char in sentence:
        if (char <= 'z' and char >= 'a'):
            embedding[string.ascii_lowercase.index(char)] += 1
        elif (char <= 'Z' and char >= 'A'):
            embedding[string.ascii_uppercase.index(char)] += 1
    return embedding, context

def getEmbedding(sentence, context):
    return noobEmbedding(sentence, context)