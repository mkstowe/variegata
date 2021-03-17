"""Variegata configuration."""
import pathlib
import os

APPLICATION_ROOT = pathlib.Path(__file__).resolve().parent.parent
VARIEGATA_ROOT = pathlib.Path(__file__).resolve().parent

DATA_ROOT = VARIEGATA_ROOT/'data'
MODEL_ROOT = VARIEGATA_ROOT/'model'
GENERATOR_ROOT = VARIEGATA_ROOT/'generator'

STATIC_DIR = VARIEGATA_ROOT/'static'
STORIES_DIR = STATIC_DIR/'stories'
GRAPHS_DIR = STATIC_DIR/'graphs'

SECRETS_FILE = APPLICATION_ROOT/'secrets.txt'