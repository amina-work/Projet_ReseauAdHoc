import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import networkx as nx
import random
import xlrd #for excel

#initializing graphs, creating multiple for later multiple algorithms testing
G = nx.Graph()
G2 = nx.Graph()

#fixate the transmission range of all nodes
rayon = 50

#Initializing the number of nodes, 
def createNodes(num):
    n_name = 1 #giving each node a diff name as Graph count similar nodes as one
    #node_sizes = []
    for i in range(num):
        #setting up the graph zone 100x100. 
        G.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
        G2.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
        n_name += 1
    
    #add node position as node attributes
    pos=nx.get_node_attributes(G,'pos')
    print(pos) #return each node x, y position
    
    #appending [x, y] of each node into a list
    list_des_xy = []
    for nd, att in pos.items():
        list_des_xy.append([att[0], att[1]])
    print(list_des_xy)
            
    #show the graphs, in diff figures
    plt.figure(1)
    nx.draw(G, pos, with_labels=True)
    plt.figure(2)
    nx.draw(G2, pos, with_labels=True)
    plt.show()

        
    
def main():
    nm = int(input("Entrer le nombre de nœuds:"))
    while nm <= 0:
        nm = int(input("Incorrect. Entrer un nombre positif de nœuds:"))
    print(createNodes(nm))
    
    
main()
#nx.draw(G)
#plt.show()

