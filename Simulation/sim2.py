import matplotlib.pyplot as plt
import networkx as nx
import random
import math

def creeNoued():
    n = int(input("Entrer le nombre des noeuds :"))
    distance = float(input("Enter le rayon de transmission: "))
    #n = 8
    #distance = 37 pixcel
    G = nx.Graph()

    for i in range(n):
        G.add_node("N" + str(i), pos=(random.randint(0, 100), random.randint(0, 100)))
        
    #G.add_edge(1, 2)
    nodes = []
    xlist = [] #pour connex
    ylist = [] #pour connex
    
    pos = nx.get_node_attributes(G,'pos')
    print("Les attributs des nœuds")
    for n,p in pos.items():
        print("Le noeud ",n," --------> x = %.2f" % p[0], " et y = %.2f" % p[1])
        nodes.append(n) #to compare to list of noueds that have voisins
        xlist.append(p[0])
        ylist.append(p[1])
        
    moyx = sum(xlist) / len(xlist)
    moyy = sum(ylist) / len(ylist)
    
    print("Calcule les distance entre les noeuds :")
    all_voisins = []
    for i, (n1, p1) in enumerate(pos.items()):
        voisins = [n1]
        for j, (n2, p2) in enumerate(pos.items()):
            dist_node = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
            if ( i != j) and (dist_node < distance) :
                voisins = voisins + [n2] 
            if j > i :
                print("La distance entre ",n1," et ",n2," = %.2f" % dist_node)
                if dist_node < distance :
                    G.add_edge(n1, n2)
        all_voisins = all_voisins + [voisins]
    #Check connexity
    for i in range(len(all_voisins)):
        if len(all_voisins[i]) == 1:
            print(all_voisins[i])
            G.remove_node(all_voisins[i][0]) #supprimer le noued sans voisins
    nx.draw(G, pos=pos,with_labels=True, node_size=600)
    plt.show()
    
    
creeNoued()