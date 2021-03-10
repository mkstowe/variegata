"""Variegata configuration."""
import pathlib
import os
# from model import create_model
# from gensim.models import Word2Vec

APPLICATION_ROOT = '/'

VARIEGATA_ROOT = pathlib.Path(__file__).resolve().parent
STATIC_DIR = VARIEGATA_ROOT/'static'
STORIES_DIR = STATIC_DIR/'stories'
GRAPHS_DIR = STATIC_DIR/'graphs'
EVENTS_LIST = STATIC_DIR/'events.csv'

DATA_ROOT = VARIEGATA_ROOT/'data'
MODEL_ROOT = VARIEGATA_ROOT/'model'
GENERATOR_ROOT = VARIEGATA_ROOT/'generator'

MODEL = None
EVENTS_DICT = None
