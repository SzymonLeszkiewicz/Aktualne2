# grafy
import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import count

from numpy.random import uniform
import random
from time import sleep
from matplotlib.animation import FuncAnimation
random.seed(11)
node_numb = 10 + 1
G = nx.Graph()

colors = nx.get_edge_attributes(G, 'color').values()
fig, ax = plt.subplots(figsize=(6,4))


def ani(p):
    x = [(random.randint(0, 100), random.randint(0, 100)) for x in range(node_numb)]
    v = {}
    for i in range(1, node_numb):
        v[i] = list(x[i])
        G.add_node(i)
        #sleep(1)
    nx.draw(G, v, edge_color=colors)
    nx.draw_networkx_labels(G, v)

v = {}
i = 1
def anim(num):
    global i
    x = (random.randint(0, 100), random.randint(0, 100))
    v[i] = list(x)
    G.add_node(i)

    i+=1
    nx.draw(G, v, edge_color=colors)
    nx.draw_networkx_labels(G, v)

ani = FuncAnimation(fig, anim, frames = 10,  interval=1000)
plt.show()
'''# TODO dodać połączenie wszystkich node z node1
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
'''