import pathlib
import os
import random
import variegata
from variegata.model import create_model, keyword_extraction
import csv


def generate_story(num_nodes):
    model = variegata.models.get_model()
    db = variegata.models.get_db().cursor()
    story_events = []

    db.execute('SELECT story_num FROM events')
    nodes = db.fetchall()

    first_node = random.choice(nodes)
    db.execute('SELECT text FROM events WHERE story_num = ?', (first_node[0],))
    curr_node = keyword_extraction.extract_keywords(db.fetchone()[0], 1)
    story_events.append(curr_node[0])

    for i in range(num_nodes - 1):
        curr_node = random.choice(model.most_similar(curr_node)[:5])[0]
        story_events.append(curr_node)

    return story_events
