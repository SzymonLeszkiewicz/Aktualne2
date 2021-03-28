import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint, seed
from time import sleep

# random.seed(99)
# node_numb = 10
# G = nx.Graph()
#
# colors = nx.get_edge_attributes(G, 'color').values()
# fig, ax = plt.subplots(figsize=(6, 4))
#
# v = {}
# i = 1
#
# def nodes(num):
#     global i
#     x = (random.randint(0, 100), random.randint(0, 100))
#     global v
#     global G
#     v[i] = list(x)
#     G.add_node(i)
#     i += 1
#     nx.draw(G, v)
#     nx.draw_networkx_labels(G, v)
#
# j = 2
# def edges1(num):
#     global j, v, G
#     colors = nx.get_edge_attributes(G, 'color').values()
#     G.add_edge(1, j, edge_color = 'r')
#     nx.draw(G, v,)
#     nx.draw_networkx_labels(G, v)
#     #for i in range(2, node_numb + 1):

#             min_dis = dis
#             min_id = y
#     # print("wynik: ", i, "   ", min_id)
#     G.add_edge(j, min_id, weight=round(min_dis,2) )
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, v, edge_labels=labels)
#     nx.draw(G, v)
#     j += 1
#
n = 6
seed(2)
cord = []
pos = {}
V = []


def wyswietlanie(spanie=0):
    l = nx.get_edge_attributes(G, 'weight')
    nl = nx.get_node_attributes(G, 'l')
    nx.draw_networkx_labels(G, pos, labels=nl)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=l)
    nx.draw(G, pos, with_labels=False, node_color='grey')
    plt.show(block=False)
    plt.pause(0.2)
    if spanie:
        sleep(3)
    plt.close()


G = nx.Graph()
nx.set_node_attributes(G, '', "l")
colors = nx.get_edge_attributes(G, 'color').values()
#     min_dis = 99999
#     min_id = -1
#     for y in range(2, node_numb):
#         if y == j:
#             continue
#         dis = math.sqrt((v[j][0] - v[y][0]) ** 2 + (v[j][1] - v[y][1]) ** 2)
#         # print(i, "   ", y, "   ", dis)
#         if dis < min_dis:
for i in range(0, n):
    V.append(i)
    G.add_node(V[i])
    G.nodes[i]['l'] = i + 1
    Vx = randint(0, 100)
    Vy = randint(0, 100)
    cord += [[Vx, Vy]]
    pos[V[i]] = [Vx, Vy]
    wyswietlanie()
    # ani = FuncAnimation(fig, nodes, frames=node_numb - 1, interval=500, repeat=False)
    # plt.show()
    #

    if i > 0:
        min = 10000
        for j in range(0, i):
            val = round(np.sqrt((cord[i][0] - cord[j][0]) ** 2 + (cord[i][1] - cord[j][1]) ** 2), 2)
            # fig, ax = plt.subplots(figsize=(6, 4))
            #
            # an = FuncAnimation(fig, edges1, frames=node_numb - 2, interval=500, repeat=False)
            # plt.show()
            if val < min:
                q1 = V[i]
                q2 = V[j]
                min = val
        G.add_weighted_edges_from([(q1, q2, min)])
        wyswietlanie()

wyswietlanie(1)
