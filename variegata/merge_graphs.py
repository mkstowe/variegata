import os
import networkx as nx


def merge_graphs():
    if os.path.exists('model/master.txt'):
        os.remove('model/master.txt')
        print("Removed master.txt")

    master_graph = nx.DiGraph()
    for filename in os.listdir('static/graphs'):
        f = os.path.join('static/graphs', filename)
        if os.path.isfile(f):
            curr_graph = nx.read_adjlist(f)
            master_graph = nx.compose(master_graph, curr_graph)

    nx.write_adjlist(master_graph, 'model/master.txt')


# merge_graphs()
