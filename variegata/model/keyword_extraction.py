import re
import string

from gensim.parsing.preprocessing import STOPWORDS
from gensim.summarization import keywords


def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def preprocess(text):
    stopwords = ['firststoryblock', 'first_story_block', 'treeid', 'tree_id', 'action', 'actions', 'action_result',
                 'result', 'results', 'context', 'null', 'actionresults', 'aresult']

    text = text.lower().strip()
    text = text.replace('\\n', ' ')
    text = decontracted(text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.translate(str.maketrans('', '', string.digits))

    result = []
    for word in text.split():
        if len(word) > 3 and word not in stopwords and word not in STOPWORDS:
            result.append(word)

    return " ".join(result)


def extract_keywords(text, num_words):
    text = preprocess(text)
    return keywords(text, words=num_words, deacc=True, lemmatize=True).replace('\n', " ").split(" ")
