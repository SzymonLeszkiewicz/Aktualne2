import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
from time import  sleep
import math
from itertools import count
from numpy.random import uniform
import random
from matplotlib.animation import FuncAnimation


l = int(input("Podaj licznosc zbioru L: "))
L = []
for i in range(l):
    L.append(input("podaj usługe dodatkowa: "))

G = nx.Graph()
colors = nx.get_edge_attributes(G, 'color').values()
G.add_edge('A', 'B')
G.add_edge('B', 'D')
G.add_edge('A', 'C')
G.add_edge('C', 'D')
G.add_edge('E', 'D')
G.add_edge('F', 'D')

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()

def usl(a, b):
    for i in G:
        pass

