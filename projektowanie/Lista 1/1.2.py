import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # empty graph

G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'D', weight=9)
G.add_edge('A', 'D', weight=9)
G.add_edge('C', 'D', weight=9)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()
