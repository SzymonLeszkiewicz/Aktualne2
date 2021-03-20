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

L = ['ap','ob']
# l = int(input("Podaj licznosc zbioru L: "))
# L = []
# for i in range(l):
#     L.append(input("podaj usługe dodatkowa: "))

G = nx.Graph()
colors = nx.get_edge_attributes(G, 'color').values()
G.add_edge('A', 'B')
G.add_edge('B', 'D')
G.add_edge('A', 'C')
G.add_edge('C', 'D')
G.add_edge('E', 'D')
G.add_edge('F', 'D')
nx.set_node_attributes(G, 'ttt', "usluga")

#print('A' in G.neighbors('B'))
#G.remove_node('D')
def usl(a, b):
    # print(type(list(a.nodes)))
    # print(list(a.nodes))
    g = random.choice(list(a.nodes))
    sasiedzi = list(a.neighbors(g))
    atrybutysa=[]
    for i in sasiedzi:
        atrybutysa.append(a.nodes[i]['usluga'])
        #atrybutysa.append()
    print(atrybutysa)
    global L
    print(L)
    czy_znalazlem = False
    for i in L:
        if i not in atrybutysa:
            a.nodes[g]['usluga'] = i

            czy_znalazlem = True
            break
    if czy_znalazlem == 0:
        print("nie mozna tak ustawić uslug")
        # i tutaj wywoluje pomiejszony zbior galeri

    print(G.nodes[g]['usluga'])
    print(sasiedzi)

    pos = nx.circular_layout(a)
    nx.draw_networkx_nodes(a, pos, node_size=250)
    nx.draw_networkx_labels(a, pos)
    nx.draw_networkx_edges(a, pos)
    plt.show()

    abezg = a.copy()
    abezg.remove_node(input("podaj cos do usuniecia"))
    return usl(abezg, 0)

usl(G, 0)
