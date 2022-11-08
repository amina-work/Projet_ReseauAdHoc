import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import networkx as nx
import math


#Initializing the number of nodes, 
def chooseNodesNum(num):
    G = nx.Graph()
    n_name = 1 #giving each node a diff name as Graph count similar nodes as one
    for i in range(num):
        G.add_node("N" + str(n_name))
        n_name += 1
    return list(G)
        
    
def main():
    nm = int(input("Entrer le nombre de nœuds:"))
    print(chooseNodesNum(nm))
    
main()
#nx.draw(G)
#plt.show()

