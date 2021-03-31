import pickle
import random

from gensim.models import Word2Vec
# import gensim
from model import keyword_extraction
from sklearn.metrics.pairwise import cosine_similarity
import sklearn
import sklearn.feature_extraction
# from pathlib import Path
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def generate_story(num_nodes):
    story_events = []

    story_nums = df.story_num.unique()
    starting_text = df.loc[df['story_num'] == random.choice(story_nums)].iloc[0]['text']

    curr_node = keyword_extraction.extract_keywords(starting_text, 1)

    query_vec = vectorizer.transform(curr_node)
    results = cosine_similarity(X, query_vec).reshape((-1,))

    for i in results.argsort()[-1:][::-1]:
        story_events.append(df.iloc[i, 1])

    for i in range(num_nodes - 1):
        curr_node = random.choice(model.wv.most_similar(curr_node)[:5])[0]
        query_vec = vectorizer.transform([curr_node])
        results = cosine_similarity(X, query_vec).reshape((-1,))

        for j in results.argsort()[-1:][::-1]:
            story_events.append(df.iloc[j, 1])

    return story_events


if __name__ == "__main__":
    model = Word2Vec.load(resource_path('model/variegata.model'))
    vectorizer = pickle.load(open(resource_path('data/vectorizer.pk'), 'rb'))
    X = pickle.load(open(resource_path('data/transformed_vec.pk'), 'rb'))
    df = pickle.load(open(resource_path('data/dataframe.pk'), 'rb'))

    for event in generate_story(10):
        print(event, '\n')
