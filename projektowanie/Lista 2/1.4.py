import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import math
from itertools import count
from numpy.random import uniform
import random
random.seed(115)
from matplotlib.animation import FuncAnimation



L = ['ap', 'ob', 'asd']
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

# G.add_edge('F', 'A')
# G.add_edge('E', 'B')
# G.add_edge('E', 'A')

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=3000)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()

nx.set_node_attributes(G, '', "usluga")

def usl(a, b):
    g = random.choice(list(a.nodes))
    a.nodes[g]['usluga'] = L[0]
    c = a.copy()
    j = 1
    for i in list(a.nodes):
        if i == g:
            continue
        sasiedzi = list(a.neighbors(i))
        atrybutysa = []
        for x in sasiedzi:
            atrybutysa.append(a.nodes[x]['usluga'])
        if L[j] in atrybutysa:
            j += 1
            if j>= len(L):
                print("tak tego nie da sie zrobic")
                c.remove_node(g)
                return usl(c, 0)
        a.nodes[i]['usluga'] = L[j]

        # for x in L:
        #    # a.nodes[x]['usluga'] = L[0]
        #     for i in list(a.nodes):
        #         if a.nodes[i]['usluga'] in atrybutysa:
        #             print('zle')

    # atrybutysa.append()
    '''print(atrybutysa)
    global L
    print(L)

    for i in list(a.nodes):
        if i == g:
            continue'''

    # czy_znalazlem = False
    # for i in L:
    #     if i not in atrybutysa:
    #         a.nodes[g]['usluga'] = i
    #         b = a.copy()
    #         czy_znalazlem = True
    #         break
    # if czy_znalazlem == 0:
    #     print("nie mozna tak ustawić uslug")
    # i tutaj wywoluje pomiejszony zbior galeri

    '''print(G.nodes[g]['usluga'])
    print(sasiedzi)'''
    pos = nx.circular_layout(a)
    node_labels = nx.get_node_attributes(a, 'usluga')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_nodes(a, pos, node_size=3000)
    #nx.draw_networkx_labels(a, pos)
    nx.draw_networkx_edges(a, pos)
    plt.show()

usl(G, G)




