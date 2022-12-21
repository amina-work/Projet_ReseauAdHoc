import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import numpy as np

def clusterAlgo():
    n = int(input("Entrer le nombre des noeuds :"))
    distance = float(input("Enter le rayon de transmission: "))
    #n = 8
    #distance = 37 pixcel
    G = nx.Graph()
    
    f = open("registre.txt", "w")
    registre = ["****************************** SIMULATION START ******************************"]
    registre.append("\n" + "\n")
    registre.append("********************* L'algorithme de Clustering *********************")
    registre.append("\n" + "\n")

    for i in range(n):
        G.add_node("N" + str(i), pos=(random.randint(0, 100), random.randint(0, 100)))
        
    #G.add_edge(1, 2)
    nodes = []
    
    pos = nx.get_node_attributes(G,'pos')
    print("Les attributs des nœuds")
    registre.append("********************* Les attributs des noueds de reseau *********************")
    registre.append("\n")
    for n,p in pos.items():
        print("Le noeud ",n," --------> x = %.2f" % p[0], " et y = %.2f" % p[1])
        registre.append("Le noued " + str(n) + " --------> x = %.2f" % p[0] + " et y = %.2f" % p[1])
        registre.append("\n")
        nodes.append(n) #to compare to list of noueds that have voisins

    registre.append("\n" + "\n")
    print("Calcule les distance entre les noeuds :")
    registre.append("********************* Calculation des distances entre les noueds de reseau *********************")
    registre.append("\n")
    all_voisins = []
    for i, (n1, p1) in enumerate(pos.items()):
        voisins = [n1]
        for j, (n2, p2) in enumerate(pos.items()):
            dist_node = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
            if ( i != j) and (dist_node < distance) :
                voisins = voisins + [n2] 
            if j > i :
                print("La distance entre ",n1," et ",n2," = %.2f" % dist_node)
                registre.append("La distance entre " + n1 + " et " +n2 + " = %.2f" % dist_node)
                registre.append("\n")
                if dist_node < distance :
                    G.add_edge(n1, n2)
        all_voisins = all_voisins + [voisins]
        
    #check connexity
    if nx.is_connected(G) == False:
         clusterAlgo()
    dict_des_voisins = {}
    print("Affichage la liste des voisin :")
    registre.append("\n" + "\n" + "\n")
    registre.append("********************* Affichage la liste des voisin *********************")
    registre.append("\n" + "\n")
    for i in range(len(all_voisins)):
        print("\nLes voisin du ", all_voisins[i][0]," sont : ", end="  ")
        registre.append("Les voisin du " + all_voisins[i][0] + " sont : ")
        dict_des_voisins[all_voisins[i][0]] = []
        #print("\n",i)
        for j in range(1,len(all_voisins[i])):
            dict_des_voisins[all_voisins[i][0]] += [all_voisins[i][j]]
            registre.append(all_voisins[i][j])
            registre.append("\t")
            print(all_voisins[i][j], end='  ')
        registre.append("\n")
    #print(dict_des_voisins)
    #Cluster Algorithm
    registre.append("\n" + "\n" + "\n" + "\n")
    registre.append("********************* L'Algorithme de Clustering *********************")
    registre.append("\n" + "\n")

    cluster = []
    #E1 - chaque noued est un valeur
    for infos in dict_des_voisins.values():
        infos.insert(0, random.randint(0, 10))
    #E3 - chaque noued comapare leur numero et ses voisins, et elect le 
    for nd, infos in dict_des_voisins.items():
        comp_list = []
        #E2 - chaque noueds va envoyer leur numero ID a ses voisins
        registre.append("\n")
        registre.append(nd + " a envoyer un message: " + nd + " est ClusterHead, avec Min=" + str(infos[0]) + " a: " + ' '.join(infos[1:]))
        registre.append("\n")
        for i in infos[1:]:
            if nd != i:
                registre.append(i + " recu le message")
                registre.append("\t\t")
                registre.append(i + " envoyer a "+ nd + ": " + str(dict_des_voisins[i][0]))
                registre.append("\t\t")
                registre.append(nd + " recu le message")
                registre.append("\n")
        print(nd, "a envoyer un message:", nd, "est ClusterHead, avec Min=", infos[0], "à:", infos[1:])

        comp_list.append(infos[0])
        for i in range(1, len(infos)):
            comp_list.append(dict_des_voisins[infos[i]][0])
        ch = comp_list.index(min(comp_list))
        if infos[ch] == infos[0]:
            registre.append("\n" + "\n")
            registre.append(nd + " a envoyer un message: "+ nd + " est ClusterHead avec Min= " + str(min(comp_list)))
            registre.append("\n")
            registre.append("de Cluster:" + ' '.join([str(i) for i in dict_des_voisins[nd] if i not in cluster]))
            registre.append("\n" + "\n")
            cluster.append(nd)
            for i in dict_des_voisins[nd]:
                if i not in cluster:
                    cluster.append(i)
                if nd != i:
                    registre.append(str(i) + " recu le message")
                    registre.append("\n")
            print(nd, "a envoyer un message:", nd, "est ClusterHead avec Min=", min(comp_list))
            print("de Cluster:", dict_des_voisins[nd])
        else:
            print(nd, "a envoyer un message:", infos[ch], "est ClusterHead avec Min=", min(comp_list))
            print("de Cluster:", dict_des_voisins[infos[ch]])

            registre.append("\n" + "\n")
            registre.append(nd + " a envoyer un message: "+ infos[ch] + " est ClusterHead avec Min= " + str(min(comp_list)))
            registre.append("\n")
            registre.append("de Cluster: " + ' '.join([str(i) for i in dict_des_voisins[infos[ch]][1:] if i not in cluster]))
            registre.append("\n")
            for i in dict_des_voisins[infos[ch]][1:]:
                if i not in cluster:
                    cluster.append(i)
                if nd != i:
                    registre.append(str(i) + " recu le message")
                    registre.append("\n")
                    
    registre.append("****************************** SIMULATION END ******************************")
    f.writelines(registre)
    f.close()
    nx.draw(G, pos=pos,with_labels=True, node_size=600)
    f = plt.show()
    
def main():
    print("****************************** SIMULATION START ******************************")
    print(clusterAlgo())
    print("****************************** SIMULATION END ******************************")
    
main()