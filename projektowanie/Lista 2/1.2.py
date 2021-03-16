# grafy
import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import count
from numpy.random import uniform
import random
from matplotlib.animation import FuncAnimation

random.seed(7)
node_numb = 10
G = nx.Graph()

colors = nx.get_edge_attributes(G, 'color').values()
fig, ax = plt.subplots(figsize=(6, 4))


def ani(p):
    x = [(random.randint(0, 100), random.randint(0, 100)) for x in range(node_numb)]
    v = {}
    for i in range(1, node_numb+1):
        v[i] = list(x[i])
        G.add_node(i)
    nx.draw(G, v, edge_color=colors)
    nx.draw_networkx_labels(G, v)

v = {}
i = 1

def nodes(num):
    global i
    x = (random.randint(0, 100), random.randint(0, 100))
    global v
    v[i] = list(x)
    G.add_node(i)
    i += 1
    nx.draw(G, v, edge_color=colors)
    nx.draw_networkx_labels(G, v)

j = 2
def edges1(num):
    global j
    global v
    colors = nx.get_edge_attributes(G, 'color').values()

    G.add_edge(1, j, color = 'black')
    nx.draw(G, v, edge_color=colors)

    nx.draw_networkx_labels(G, v)
    j += 1
    print("halo")

    nx.draw_networkx_labels(G, v)

ani = FuncAnimation(fig, nodes, frames=node_numb-1, interval=50, repeat = False)

plt.show()
fig, ax = plt.subplots(figsize=(6, 4))

an = FuncAnimation(fig, edges1, frames=node_numb-2, interval=50, repeat = False)
plt.show()

'''for i in range(2, node_numb+1):
    G.add_edge(1, i, color = 'black')

for i in range(2, node_numb + 1 ):
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

nx.draw(G, v, edge_color=colors)
nx.draw_networkx_labels(G, v)
plt.show()
'''
