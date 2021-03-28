import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance
from math import sqrt

B= nx.Graph()
G = nx.Graph()
colors = nx.get_edge_attributes(G, 'color').values()
G.add_edge('A', 'B')
G.add_edge('B', 'D')
G.add_edge('A', 'C')
G.add_edge('C', 'D')
G.add_edge('E', 'D')
G.add_edge('F', 'D')

G.add_edge('F', 'A')
G.add_edge('E', 'B')
G.add_edge('E', 'A')
G.add_edge('E', 'F')

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1900)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
def eukli(t, r):
    dis = sqrt((t[0] - r[0]) ** 2 + (t[1] - r[1]) ** 2)
    return round(dis, 2)

def dist(n1, n2):  # 1.3
    road = nx.shortest_path(G, source=n1, target=n2)
    distanc = 0
    print(road)
    for i in range(len(road)-1):
        distanc += eukli(pos[road[i]], pos[road[i+1]])
    print(distanc)
dist('C', 'F')
