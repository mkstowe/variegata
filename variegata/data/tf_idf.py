import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path

def tf_idf():
    here = Path(__file__).parent
    print("Reading Events")
    df = pd.read_csv(here / 'events.csv')

    print("Creating Vectorizer")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['text'].values.astype('U'))

    print("Dumping Pickles")
    pickle.dump(df, open(here / 'dataframe.pk', 'wb'))
    pickle.dump(vectorizer, open(here / 'vectorizer.pk', 'wb'))
    pickle.dump(X, open(here / 'transformed_vec.pk', 'wb'))


if __name__ == "__main__":
    tf_idf()
