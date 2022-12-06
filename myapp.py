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
    print("\n\n \t\t\tSIMULATION START \n\n")
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
    voisins_uni = {}
    for nd, att in pos.items():
        for nd2, att2 in pos.items():
            if nd != nd2:
                if att != att2:
                    #calculate the euclidien distance
                    distance = math.dist(att, att2)
                    if distance not in list_of_eds:
                        if distance < rayon:
                            print(nd, "and", nd2, "are neighbors")
                            G.add_edge(nd, nd2)
                            voisin.append([nd, nd2, distance])
                            voisins_uni[nd] = [nd].append(nd2)
                    list_of_eds.append([nd, nd2, distance])
    print(rayon) #le rayon pour tous les noueds (UDG)
    print(voisin) #le noued, et le list de ses voisins
    print(list_of_eds) #le list de distance entre tous les noueds
     
    #show the graphs, in diff figures
    nx.draw(G, pos, with_labels=True)
    #plt.figure(2)
    #nx.draw(G2, pos, with_labels=True)
    #plt.show()
    print("\n\n \t\t\tSIMULATION END \n\n")

        
    
def main():
    nm = int(input("Entrer le nombre de nœuds:"))
    while nm <= 0:
        nm = int(input("Incorrect. Entrer un nombre positif de nœuds:"))
    print(createNodes(nm))

main()
plt.show()
