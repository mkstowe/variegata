"""Insta485 package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (variegata/data/config.py)
app.config.from_object('data.config')

app.config.from_envvar('VARIEGATA_DATA_SETTINGS', silent=True)

import data.views  # noqa: E402  pylint: disable=wrong-import-position