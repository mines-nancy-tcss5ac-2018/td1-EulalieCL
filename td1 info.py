# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""projet euler 16"""
def solve(x):
    somme = 0
    chaine = str(x)
    for i in chaine:
       somme += int(i) 
    return somme
       
       
assert solve(2**15)== 26

print(solve(2**1000))

"""projet euler 22"""

def solve():

    fichier=open("listenoms.txt","r")
    for ligne in fichier:
        texte = ligne
    fichier.close() ##création chaîne de caractère correspondant au contenu du fichier
    listenoms=texte.split(",") ##création liste des noms
    listenoms2=sorted(listenoms)
    
    alphabet='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'  ##les guillemets " prendront la valeur 0
    somme = 0
    
    for i in range(len(listenoms2)):
        sum =0      ##name score de chaque nom
        
        for j in listenoms2[i]:
            sum+=alphabet.find(j)
        somme += sum*(i+1)    ##on somme les namescore multiplié par la position du nom dans la liste
    
    return somme    
        
print(solve())


"""Projet euler 5"""

def solve():
    nb=0     ##nb est le nombre de Lychrel numbers
    for i in range(1,10001):
        k=i
        l=0
        k=k+reverse(k)
        while palindrome(k)==False and l<50:
            k=k+reverse(k)
            l+=1
        if palindrome(k):     ##on vérifie que la boucle s'est arrêté car on est tombé sur un palindrome et pas parce qu'on a atteint les 50 itérations
                nb+=1
    return 10000-nb


def reverse(x):
    texte = str(x)
    rev=''
    n=len(texte)
    for i in range(0,n):
        rev = rev+texte[n-i-1]
    inverse=int(rev)
    return inverse


   
   
def palindrome(x):
    nombre=str(x)
    n=len(nombre)
    for i in range (0,n):
        if nombre[i]!=nombre[n-i-1]:
            return False
    else:
        return True



print(solve())

