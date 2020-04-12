import numpy as np
import string
import modules.glove as glove

def noobEmbedding(sentence, context):
    embedding = np.zeros(26)
    for char in sentence:
        if (char <= 'z' and char >= 'a'):
            embedding[string.ascii_lowercase.index(char)] += 1
        elif (char <= 'Z' and char >= 'A'):
            embedding[string.ascii_uppercase.index(char)] += 1
    return embedding, context

def getEmbedding(sentence, context):
    return gloveEmbedding(sentence, context)

def gloveEmbedding(sentence, context):
    words = sentence.split()
    if words:
        vectors = np.stack([glove.MODEL[k] if k in glove.MODEL else glove.DEFAULT for k in words],axis=1)
        embedding = np.mean(vectors,axis = 1)
    else:
        embedding = glove.DEFAULT
    return embedding, context
    
    