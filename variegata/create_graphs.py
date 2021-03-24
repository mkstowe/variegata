import os
import networkx as nx


def merge_graphs():
    master_graph = nx.MultiDiGraph()
    for filename in os.listdir('static/graphs'):
        f = os.path.join('static/graphs', filename)
        if os.path.isfile(f):
            curr_graph = nx.read_gml(f)
            master_graph = nx.compose(master_graph, curr_graph)

    return master_graph


def create_keyword_graph(in_graph):
    kw_graph = nx.MultiDiGraph()
    for u, v in in_graph.edges(data=False, keys=False):
        kw_1 = in_graph.nodes[u]['keywords']
        kw_2 = in_graph.nodes[v]['keywords']

        for i in kw_1:
            for j in kw_2:
                kw_graph.add_edge(i, j)

    return kw_graph


def construct_graph():
    if os.path.exists('model/kw_graph.gml'):
        os.remove('model/kw_graph.gml')
        print("Removed kw_graph.gml")

    nx.write_gml(create_keyword_graph(merge_graphs()), 'model/kw_graph.gml')


# merge_graphs()
