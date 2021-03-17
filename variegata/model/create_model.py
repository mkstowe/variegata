import networkx as nx
from node2vec import Node2Vec
import os


def create_model():
    if not os.path.exists('model/master.txt'):
        print("master.txt does not exist")
        return

    g = nx.read_adjlist('model/master.txt')
    node2vec = Node2Vec(g, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    if os.path.exists('model/variegata.model'):
        os.remove('model/variegata.model')
        print("Removed variegata.model")

    model.save('model/variegata.model')

    print("Saved model")
