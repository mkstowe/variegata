"""Variegata package initializer."""
import flask
import os

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (variegata/data/config.py)
app.config.from_object('variegata.config')
app.config.from_envvar('VARIEGATA_SETTINGS', silent=True)

import variegata.flask_models  # noqa: E402  pylint: disable=wrong-import-position
import variegata.views  # noqa: E402  pylint: disable=wrong-import-position
