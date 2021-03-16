# grafy
import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.random import uniform
import random


def los_wierz(node_numb):
    x = [(random.randint(0, 100), random.randint(0, 100)) for x in range(node_numb)]
    v = {}
    for i in range(1, node_numb):
        v[i] = list(x[i])
    G.add_nodes_from([i for i in range(1, node_numb)])
    return v


node_numb = 10 + 1
G = nx.Graph()
v = los_wierz(node_numb)
G.add_nodes_from([i for i in range(1, node_numb)])
# TODO dodać połączenie wszystkich node z node1
# TODO dla każdego noda dodać najkrotsze połączenie
for i in range(2, node_numb):
    G.add_edge(1, i, color = 'black')

for i in range(2, node_numb ):
    min_dis = 99999
    min_id = -1

    for y in range(2, node_numb):
        if y == i:
            continue
        dis = math.sqrt((v[i][0] - v[y][0]) ** 2 + (v[i][1] - v[y][1]) ** 2)
        #print(i, "   ", y, "   ", dis)
        if dis < min_dis:
            min_dis = dis
            min_id = y
    #print("wynik: ", i, "   ", min_id)
    G.add_edge(i, min_id, color='r')

colors = nx.get_edge_attributes(G, 'color').values()
nx.draw(G, v, edge_color=colors)
nx.draw_networkx_labels(G, v)
plt.show()
