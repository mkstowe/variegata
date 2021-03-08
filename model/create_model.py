import pathlib
import networkx as nx
from node2vec import Node2Vec
import random
from gensim.models import Word2Vec


def create_model():
    g = nx.read_adjlist('master.txt')
    node2vec = Node2Vec(g, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    model.save('variegata.model')
