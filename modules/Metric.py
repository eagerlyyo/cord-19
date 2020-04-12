import numpy as np

def cosineSimilarity(a, b):
    normAB = np.linalg.norm(a)*np.linalg.norm(b)
    if normAB != 0:
        return np.dot(a, b)/(normAB)
    else:
        return 0

def similarity(a, b):
    return cosineSimilarity(a, b)