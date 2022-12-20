import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
import os
from tkinter import filedialog, Text

#Implementing the GUI
#root = tk.Tk()

#canvas = tk.Canvas(root, height=500, width=500, bg="blue")
#canvas.pack()

#frame = tk.Frame(root, bg="#D3D3D3")
#frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

#root.mainloop()
#Implementing the GUI end


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
    
    pos = nx.get_node_attributes(G,'pos')
    print("Les attributs des nœuds")
    for n,p in pos.items():
        print("Le noeud ",n," --------> x = %.2f" % p[0], " et y = %.2f" % p[1])
        nodes.append(n) #to compare to list of noueds that have voisins

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
        
    #check connexity
    if nx.is_connected(G) == False:
         creeNoued()
    print("Affichage la liste des voisin :")
    for i in range(len(all_voisins)):
        print("\nLes voisin du ", all_voisins[i][0]," sont : ", end="  ")
        #print("\n",i)
        for j in range(1,len(all_voisins[i])):
            print(all_voisins[i][j], end=' and ')

    nx.draw(G, pos=pos,with_labels=True, node_size=600)
    plt.show()
    
def main():
    print("****************************** SIMULATION START ******************************")
    print(creeNoued())
    print("****************************** SIMULATION END ******************************")
    
main()