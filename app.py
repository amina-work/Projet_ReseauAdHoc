import matplotlib.pyplot as plt
import networkx as nx
import random
import math

G = nx.Graph()

rayon = 50

n_name = 1 #giving each node a diff name as Graph count similar nodes as one
    #node_sizes = []
num = int(input("Donnez le nombre des noueds:"))
for i in range(num):
    #setting up the graph zone 100x100. 
    G.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
    n_name += 1
pos=nx.get_node_attributes(G,'pos')
print(pos)
for nd, att in pos.items():
    for nd2, att2 in pos.items():
        if att != att2:
            distance = math.dist(att, att2)
            if distance < rayon:
                print(nd, "and", nd2, "are neighbors")
                G.add_edge(nd, nd2)

nx.draw(G, pos, with_labels=True)
plt.show()