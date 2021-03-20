import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
from numpy.random import uniform
import random
G = nx.Graph()
node_num = 400


x = [(random.randint(0,10), random.randint(0,10))]
for i in range(1, node_num):
    x.append((random.randint(0,10), random.randint(0,10)))
    l = 1
    while x[i] == x[i - 1] and l < 100:
        x.pop(-1)
        l += 1
        x.append((random.randint(0,10), random.randint(0,10)))

if l == 100:
    print("zadanie nie powiodło się")
else:
    v = {}
    for i in range(1, node_num):
        v[i] = list(x[i])
    G.add_nodes_from([i for i in range(1, node_num)])
    nx.draw(G, v)
    plt.show()