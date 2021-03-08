"""Variegata Data package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (variegata/data/config.py)
app.config.from_object('generator.config')
app.config.from_envvar('GENERATOR_SETTINGS', silent=True)

# import generator.views  # noqa: E402  pylint: disable=wrong-import-position
