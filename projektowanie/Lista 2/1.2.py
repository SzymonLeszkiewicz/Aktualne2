# grafy
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

random.seed(99)
node_numb = 10
G = nx.Graph()

colors = nx.get_edge_attributes(G, 'color').values()
fig, ax = plt.subplots(figsize=(6, 4))

v = {}
i = 1

def nodes(num):
    global i
    x = (random.randint(0, 100), random.randint(0, 100))
    global v
    global G
    v[i] = list(x)
    G.add_node(i)
    i += 1
    nx.draw(G, v)
    nx.draw_networkx_labels(G, v)

j = 2
def edges1(num):
    global j, v, G
    colors = nx.get_edge_attributes(G, 'color').values()
    G.add_edge(1, j, edge_color = 'r')
    nx.draw(G, v,)
    nx.draw_networkx_labels(G, v)

    #for i in range(2, node_numb + 1):
    min_dis = 99999
    min_id = -1
    for y in range(2, node_numb):
        if y == j:
            continue
        dis = math.sqrt((v[j][0] - v[y][0]) ** 2 + (v[j][1] - v[y][1]) ** 2)
        # print(i, "   ", y, "   ", dis)
        if dis < min_dis:
            min_dis = dis
            min_id = y
    # print("wynik: ", i, "   ", min_id)
    G.add_edge(j, min_id, weight=round(min_dis,2) )
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, v, edge_labels=labels)
    nx.draw(G, v)
    j += 1

ani = FuncAnimation(fig, nodes, frames=node_numb-1, interval=250, repeat = False)
plt.show()

fig, ax = plt.subplots(figsize=(6, 4))
an = FuncAnimation(fig, edges1, frames=node_numb-2, interval=250, repeat = False)
plt.show()
