import networkx as nx
import matplotlib.pyplot as plt

node_num = 8
G = nx.complete_graph(node_num)  # empty graph
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
