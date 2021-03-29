import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('events.csv')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

pickle.dump(df, open('dataframe.pk', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pk', 'wb'))
pickle.dump(X, open('transformed_vec.pk', 'wb'))
