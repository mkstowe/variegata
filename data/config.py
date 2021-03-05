"""Variegata data configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

VARIEGATA_DATA_ROOT = pathlib.Path(__file__).resolve().parent
STORIES_DIR = VARIEGATA_DATA_ROOT/'static'/'stories'
GRAPHS_DIR = VARIEGATA_DATA_ROOT/'static'/'graphs'
EVENTS_LIST = VARIEGATA_DATA_ROOT/'static'/'events.csv'
