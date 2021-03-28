import networkx as nx
import networkx.drawing as nxd
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import math
from itertools import count
from numpy.random import uniform
import random
random.seed(51)
from matplotlib.animation import FuncAnimation


L = ['apteka', 'piekarnia', 'komputerowy']
# l = int(input("Podaj licznosc zbioru L: "))
# L = []
# for i in range(l):
#     L.append(input("podaj usługe dodatkowa: "))

B= nx.Graph()
G = nx.Graph()
colors = nx.get_edge_attributes(G, 'color').values()
G.add_edge('A', 'B')
G.add_edge('B', 'D')
G.add_edge('A', 'C')
G.add_edge('C', 'D')
G.add_edge('E', 'D')
G.add_edge('E', 'A')
G.add_edge('E', 'B')

'''
G.add_edge('E', 'A')
G.add_edge('E', 'F')'''

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1900)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.title('UŁOŻENIE GALERII')

plt.show()

nx.set_node_attributes(G, '', "usluga")

def usl(a, b):
    g = random.choice(list(a.nodes))
    print("wylosowano: ", g)
    a.nodes[g]['usluga'] = L[0]
    c = a.copy()
    global B
    for i in list(a.nodes):
        j = 0
        if i == ord(g)-65:
            continue
        sasiedzi = list(a.neighbors(i))
        atrybutysa = []
        for x in sasiedzi:
            atrybutysa.append(a.nodes[x]['usluga'])
        for x in range(len(L)):
            if L[x] not in atrybutysa:
                j=x
                break
            if L[x] in atrybutysa:
                # j += 1
                if x== len(L)-1:
                    pos = nx.spring_layout(a)
                    node_labels = nx.get_node_attributes(a, 'usluga')
                    print('asdfasdf',node_labels)
                    nx.draw_networkx_labels(G, pos, labels=node_labels)
                    nx.draw_networkx_nodes(a, pos, node_size=1900, node_color='red')
                    nx.draw_networkx_labels(a, pos)
                    nx.draw_networkx_edges(a, pos)
                    plt.title('Rozwiązanie niedopuszczalne')
                    plt.show()
                    c.remove_node(g)
                    return usl(c, B)
        a.nodes[i]['usluga'] = L[j]

    pos = nx.spring_layout(a)
    node_labels = nx.get_node_attributes(a, 'usluga')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_nodes(a, pos, node_size=1900)
    #nx.draw_networkx_labels(a, pos)
    nx.draw_networkx_edges(a, pos)
    plt.show()

usl(G, G)




