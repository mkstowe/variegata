import pathlib
import networkx as nx
from node2vec import Node2Vec
import random
from gensim.models import Word2Vec


def create_model():
    g = nx.read_adjlist('../model/master.txt')
    node2vec = Node2Vec(g, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    model.save('model.model')


def events_to_dict():
    event_dict = {}
    with open(pathlib.Path(__file__).resolve().parent.parent/'data'/'static'/'events.csv') as file:
        for line in file:
            split_line = line.split(',')
            if split_line[0] not in event_dict:
                event_dict[split_line[0]] = [split_line[2]]
            else:
                event_dict[split_line[0]].append(split_line[2])

    return event_dict


# create_model()
MODEL = Word2Vec.load('model.model')
EVENTS = events_to_dict()


def generate_story(num_nodes):
    story_events = []
    cur_node = str(random.choice(list(EVENTS.keys()))) + "_0"
    for i in range(num_nodes):
        cur_node = MODEL.wv.most_similar(cur_node)[0][0]
        split_node = cur_node.split("_")
        story_events.append(EVENTS[split_node[0]][int(split_node[1])])

    return story_events


print(generate_story(2))
