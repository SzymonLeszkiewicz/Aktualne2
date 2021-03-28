import networkx as nx
import matplotlib.pyplot as plt
from math import floor
import sys

# siatka NxK
N = 200
K = 100
# odleglosc punktów na siatce
D = 10
# minimalna odleglosc między odwiertami
S = 15
# ilość owietrów
R = 50
G = nx.Graph()
cord_x = list(range(0, N + 1, D))
cord_y = list(range(0, K + 1, D))
print(cord_x)
print(cord_y)

m = D


def pos():
    w = 0
    k = 0
    p = dict()
    for n in range(len(cord_x) * len(cord_y) // 1):
        G.add_node(n)
        w1 = cord_x[w]
        k1 = cord_y[k]
        w += 1
        # for n in range(roz):
        #     G.add_node(n)
        #     t = r[w]
        #     k = r[k]
        #     w += 1
        if w == len(cord_x):
            w = 0

            k += 1
        #     k = r[k]
        #     w += 1
        p[n] = [w1, k1]
    return p


J = nx.Graph()
# x.draw_networkx_labels(J, pos, labels=node_labels)
#                     nx.draw_networkx_nodes(J, pos, node_color='red')
#                     nx.draw_networkx_labels(J, pos)
#                     nx.draw_networkx_edges(J, pos)
for i in range(R):
    J.add_node(i, weight='proba')
    # for n in J.nodes():
    #     wierz.append(n)
    #     nei = list(J.neighbors(n))
wierz = list(J.nodes)

jp = {}
def odwierty():
    # he = bool(1)
    kolumna = 0
    gg = len(wierz)
    wiersz = 1
    he = 1
    j = list(J.nodes())
    print("j", j)
    pierwszy = 1
    for j_node in j:
        if pierwszy:
            gg = len(wierz)
            # wiersz = 1
            # he = 1
            wp = 0
            kp = 0
            jp[j_node] = [wp, kp]
            pierwszy = 0
        else:
            kolumna = 0
            kp = jp[j_node - 1][1]
            # pom = 0
            # print(kp)
            gg = len(wierz)
            if he:
                wp = jp[j_node - 1][0] + S
                while wp % m:
                    wp += 1
                if wp > N:
                    he = 0
                    wiersz += 1
                    wp = 200  # sdfasdasd
                    kp += S
                    while kp % m:
                        kp += 1
            else:
                wp = jp[j_node - 1][0] - S
                while wp % m != 0:
                    wp -= 1
                if wp < 0:
                    kolumna = wiersz // 2
                    # kolumna +=1
                    wiersz += 1
                    wp, he = 0, 1
                    kp += S
                    while kp % m:
                        kp = kp + 1

            if kp > K:
                print("zle")
                sys.exit()

            jp[j_node] = [wp, kp]
    free_row = []


odwierty()
print(jp)
#     nx.draw_networkx_labels(G, pos, labels=node_labels)
#     nx.draw_networkx_nodes(a, pos, node_size=1900)
#     #nx.draw_networkx_labels(a, pos)
#     nx.draw_networkx_edges(a, pos)
nx.draw(G, pos(), node_size=150, with_labels=False, node_color='grey')
nx.draw(J, jp, node_size=90, with_labels=False, node_color='red')
plt.show()
