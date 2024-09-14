from nltk import download as nltk_download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import heapq

nltk_download('punkt_tab')
nltk_download('stopwords')

def summarize(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    fdist = FreqDist(filtered_words)

    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in fdist:
                if i in sentence_scores:
                    sentence_scores[i] += fdist[word]
                else:
                    sentence_scores[i] = fdist[word]
    
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    return ' '.join([sentences[i] for i in summary_sentences])
