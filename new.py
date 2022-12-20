import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input("Entrer le nombre des noeuds :"))
distance = float(input("Enter le rayon de transmission (entre 50 et 70) : "))
#n = 8
#distance = 37 pixcel
G = nx.Graph()

nodes = list("")
for i in range(n):
    nodes.append(lettres[i])  
G.add_nodes_from(nodes)

pos = dict()
for i in range(n):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    pos[lettres[i]] = (x,y)

#G.add_edge(1, 2)

for n,p in pos.items():
    print("Le noeud ",n," --------> x = %.2f" % p[0], " et y = %.2f" % p[1])

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
print("Affichage la liste des voisin :")
for i in range(len(all_voisins)):
    print("\nLes voisin du ", all_voisins[i][0]," sont : ", end="  ")
    #print("\n",i)
    for j in range(1,len(all_voisins[i])):
        print(all_voisins[i][j], end=' ')
            

nx.draw(G, pos=pos,with_labels=True, node_size=600)
plt.show()