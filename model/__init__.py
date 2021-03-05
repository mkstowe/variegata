"""Insta485 package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (variegata/model/config.py)
app.config.from_object('model.config')
app.config.from_envvar('VARIEGATA_MODEL_SETTINGS', silent=True)
