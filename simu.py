import networkx as nx
#import matplotlib.pyplot as plt


G = nx.Graph() 

nbre_nodes = int(input("Donnez le nombre des noueds: "))
name_nodes = 1
while nbre_nodes < 1:
    nbre_nodes = int(input("Incorrect. Donnez le nombre des noueds: "))

for i in range(nbre_nodes):
    G.add_node(name_nodes)
    name_nodes += 1



nx.draw(G)
#plt.show()

