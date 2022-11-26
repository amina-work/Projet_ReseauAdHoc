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
        

#nx.draw(G, pos, with_labels=True)
#plt.show()