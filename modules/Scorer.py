import modules.Embeddings as Embeddings
import modules.Tokenizer as Tokenizer
import modules.Metric as Metric

def rateParagraph(para, embeddingQuery):
    score = 0
    sentences = Tokenizer.getSentences(para)
    context = [0]
    for sentence in sentences:
        embeddingSentence, context = Embeddings.getEmbedding(sentence, context)
        score += Metric.similarity(embeddingQuery, embeddingSentence)
    return score/len(sentences)

def score(paper, query):
    result = {}

    context = [0]
    embeddingQuery, _ = Embeddings.getEmbedding(query, context)

    maxScore = 0
    resultAbstract = []
    for idx, para in enumerate(paper['abstract']):
        score = rateParagraph(para['text'], embeddingQuery)
        resultAbstract.append({'idx' : idx, 'score' : score})
        maxScore = max(maxScore, score)
    
    resultBody = []
    for idx, para in enumerate(paper['body_text']):
        score = rateParagraph(para['text'], embeddingQuery)
        resultBody.append({'idx' : idx, 'score' : score})
        maxScore = max(maxScore, score)
    resultAbstract.sort(key = lambda x:x['score'], reverse=True)
    resultBody.sort(key = lambda x:x['score'], reverse=True)

    result['abstract'] = resultAbstract
    result['body'] = resultBody
    result['score'] = maxScore
    return result