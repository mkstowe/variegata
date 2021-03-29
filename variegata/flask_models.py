import os
import pickle
import sys

import flask
import mariadb
import variegata
from gensim.models import Word2Vec


def get_db():
    if 'mariadb_db' not in flask.g:
        with open(variegata.app.config["SECRETS_FILE"], "r") as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()

        try:
            flask.g.mariadb_db = mariadb.connect(
                user=username,
                password=password,
                host="127.0.0.1",
                port=3306,
                database="mkstrnrc_variegata_stories"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    return flask.g.mariadb_db


def get_model():
    if 'model' not in flask.g:
        try:
            flask.g.model = Word2Vec.load(str(variegata.app.config["MODEL_ROOT"] / 'variegata.model'))
        except os.error as e:
            print(f"Error loading model: {e}")
            sys.exit(1)

    return flask.g.model


def get_vectorizer():
    if 'vectorizer' not in flask.g:
        try:
            flask.g.vectorizer = pickle.load(open(str(variegata.app.config["DATA_ROOT"] / 'vectorizer.pk'), 'rb'))
        except os.error as e:
            print(f"Error loading vectorizer: {e}")
            sys.exit(1)

    return flask.g.vectorizer


def get_transformed_vectorizer():
    if 'trans_vec' not in flask.g:
        try:
            flask.g.trans_vec = pickle.load(open(str(variegata.app.config["DATA_ROOT"] / 'transformed_vec.pk'), 'rb'))
        except os.error as e:
            print(f"Error loading vectorizer: {e}")
            sys.exit(1)

    return flask.g.trans_vec


def get_dataframe():
    if 'df' not in flask.g:
        try:
            flask.g.df = pickle.load(open(str(variegata.app.config["DATA_ROOT"] / 'dataframe.pk'), 'rb'))
        except os.error as e:
            print(f"Error loading vectorizer: {e}")
            sys.exit(1)

    return flask.g.df


@variegata.app.teardown_appcontext
def close_db(error):
    assert error or not error  # Needed to avoid superfluous style error
    mariadb_db = flask.g.pop('mariadb_db', None)
    if mariadb_db is not None:
        mariadb_db.commit()
        mariadb_db.close()
