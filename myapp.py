import matplotlib.pyplot as plt
import networkx as nx
import random
import math

#initializing graphs, creating multiple for later multiple algorithms testing
G = nx.Graph() #Vecteur 
G2 = nx.Graph() #OLSR

#Generate a random number 
rayon = random.randint(50, 70)

#Initializing the number of nodes, 
def createNodes(num):
    n_name = 1 #giving each node a diff name as Graph count similar nodes as one
    #node_sizes = []
    for i in range(num):
        #setting up the graph zone 100x100. 
        G.add_node("N" + str(n_name), pos=(random.randint(0, 70), random.randint(0, 70)))
        #G2.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
        n_name += 1
    
    #add node position as node attributes
    pos=nx.get_node_attributes(G,'pos')
    print(pos) #return each node x, y position
    
    #finding each 
    list_of_eds = [] #to avoid remaking arcs between same nodes
    voisin = []
    voisins = []
    voisins_uni = {}
    for nd, att in pos.items():
        for nd2, att2 in pos.items():
            if att != att2:
                #calculate the euclidien distance
                distance = math.dist(att, att2)
                if distance not in list_of_eds:
                    if distance < rayon:
                        print(nd, "and", nd2, "are neighbors")
                        G.add_edge(nd, nd2)
                        voisin.append([nd2, distance])
                list_of_eds.append(distance)
        #removing repeated neighbors from list of neighbors
        for i in voisin:
            if i not in voisins:
                voisins.append(i)
        voisins_uni[nd] = voisins
    print(rayon)
    print(voisins_uni)
            
    #show the graphs, in diff figures
    nx.draw(G, pos, with_labels=True)
    #plt.figure(2)
    #nx.draw(G2, pos, with_labels=True)
    #plt.show()

        
    
def main():
    nm = int(input("Entrer le nombre de nœuds:"))
    while nm <= 0:
        nm = int(input("Incorrect. Entrer un nombre positif de nœuds:"))
    print(createNodes(nm))

main()
plt.show()
