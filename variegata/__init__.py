"""Variegata package initializer."""
import flask
import os
from gensim.models import Word2Vec

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (variegata/data/config.py)
app.config.from_object('variegata.config')
app.config.from_envvar('VARIEGATA_SETTINGS', silent=True)

import variegata.views  # noqa: E402  pylint: disable=wrong-import-position
