import data
import model
import os
import networkx as nx


master_graph = nx.DiGraph()
for filename in os.listdir(data.app.config["GRAPHS_DIR"]):
    f = os.path.join(str(data.app.config["GRAPHS_DIR"]), filename)
    if os.path.isfile(f):
        curr_graph = nx.read_adjlist(f)
        master_graph = nx.compose(master_graph, curr_graph)

nx.write_adjlist(master_graph, str(model.app.config["MODEL_ROOT"]/'master.txt'))
