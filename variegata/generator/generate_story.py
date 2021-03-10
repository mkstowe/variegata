import pathlib
import os
import random
from gensim.models import Word2Vec
import variegata
from variegata.model import create_model
import csv


def events_to_dict():
    if not os.path.exists(pathlib.Path(__file__).resolve().parent.parent/'static'/'events.csv'):
        print("events.csv does not exist")
        return

    event_dict = {}
    with open(pathlib.Path(__file__).resolve().parent.parent/'static'/'events.csv') as file:
        for line in csv.DictReader(file, fieldnames=["story", "event_idx", "text"], quotechar='"', delimiter=',',
                                   quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if line['story'] not in event_dict:
                event_dict[line['story']] = [line['text']]
            else:
                event_dict[line['story']].append(line['text'])

    return event_dict


if os.path.exists(variegata.app.config["MODEL_ROOT"]/'variegata.model'):
    variegata.app.config["MODEL"] = Word2Vec.load(str(variegata.app.config["MODEL_ROOT"]/'variegata.model'))
else:
    create_model.create_model()
    variegata.app.config["MODEL"] = Word2Vec.load(str(variegata.app.config["MODEL_ROOT"] / 'variegata.model'))

variegata.app.config["EVENTS_DICT"] = events_to_dict()

model = variegata.app.config["MODEL"]
events_dict = events_to_dict()


def generate_story(num_nodes):
    story_events = []
    cur_node = str(random.choice(list(events_dict.keys()))) + "_0"
    for i in range(num_nodes):
        cur_node = random.choice(model.most_similar(cur_node)[:10])[0]
        split_node = cur_node.split("_")
        story_events.append(events_dict[split_node[0]][int(split_node[1])])

    return story_events
