import matplotlib.pyplot as plt
import networkx as nx
import random
import math

#initializing graphs, creating multiple for later multiple algorithms testing
G = nx.Graph() #Vecteur 
G2 = nx.Graph() #OLSR

#Generate a random number 
rayon = random.randint(30, 70)

#Initializing the number of nodes, 
def createNodes(num):
    n_name = 1 #giving each node a diff name as Graph count similar nodes as one
    #node_sizes = []
    for i in range(num):
        #setting up the graph zone 100x100. 
        G.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
        #G2.add_node("N" + str(n_name), pos=(random.randint(0, 100), random.randint(0, 100)))
        n_name += 1
    
    #add node position as node attributes
    pos=nx.get_node_attributes(G,'pos')
    print(pos) #return each node x, y position
    
    #appending [x, y] of each node into a list
    list_des_xy = []
    list_des_noueds = []
    for nd, att in pos.items():
        list_des_xy.append([att[0], att[1]])
        list_des_noueds.append(nd)
    print(list_des_noueds)
    print(list_des_xy)
    for nd in list_des_xy: #resigining each [x, y] to their node
        for nd2 in list_des_xy:
            if nd != nd2: #so it doesn"t count the distance with itself
                print(nd, nd2)
                distance = math.dist(nd, nd2)
                print(math.dist(nd, nd2)) #calculating the Euclidean distance
                if distance < rayon:
                    print(nd, "et", nd2, "sont des voisins.")
        
    print(rayon)
            
    #show the graphs, in diff figures
    #plt.figure(1)
    #nx.draw(G, pos, with_labels=True)
    #plt.figure(2)
    #nx.draw(G2, pos, with_labels=True)
    #plt.show()

        
    
def main():
    nm = int(input("Entrer le nombre de nœuds:"))
    while nm <= 0:
        nm = int(input("Incorrect. Entrer un nombre positif de nœuds:"))
    print(createNodes(nm))
    
    
main()
#nx.draw(G)
#plt.show()

