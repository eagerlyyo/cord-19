import numpy as np
import io

def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    embeddings_index = {}
    f = io.open(gloveFile, 'r', encoding="utf-8")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()
    print("Done.",len(embeddings_index)," words loaded!")
    return embeddings_index

def loadGloveEmbedding():
    MODEL = loadGloveModel("D:\cord-19\cord-19\data\glove\glove_6B_50d.txt")
    DEFAULT = np.mean([MODEL[k] for k in MODEL],axis = 0)
    return MODEL,DEFAULT

MODEL,DEFAULT = loadGloveEmbedding()


