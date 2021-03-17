import pathlib
import os
import random
import variegata
from variegata.model import create_model
import csv


def generate_story(num_nodes):
    model = variegata.models.get_model()
    db = variegata.models.get_db().cursor()
    story_events = []

    db.execute('SELECT * FROM events WHERE event_idx = 0')
    nodes = db.fetchall()

    first_node = random.choice(nodes)
    story_events.append(first_node[3])
    curr_node = first_node[1] + "_0"

    for i in range(num_nodes - 1):
        curr_node = random.choice(model.most_similar(curr_node)[:5])[0]
        split_node = curr_node.split("_")
        db.execute(
            'SELECT text FROM events WHERE (story_num = ? AND event_idx = ?)',
            (split_node[0], int(split_node[1]),)
        )
        curr_text = db.fetchone()[0]
        story_events.append(curr_text)

    return story_events
